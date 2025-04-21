import cv2
import string
import os

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Load the image
x = cv2.imread(r"C:\Users\ASUS\Downloads\Steganography-master\Steganography-master\istockphoto-517188688-1024x1024.jpg")

# Check if the image was loaded successfully
if x is None:
    print("Error: Unable to load the image file. Please check the file path or ensure the file exists.")
    exit()

i = x.shape[0]
j = x.shape[1]
print(f"Image dimensions: {i}x{j}")

key = input("Enter key to edit (Security Key): ")
text = input("Enter text to hide: ")

kl = 0
z = 0  # decides plane
n = 0  # number of row
m = 0  # number of column

l = len(text)

# Encoding the text into the image
for i in range(l):
    x[n, m, z] = d[text[i]] ^ d[key[kl]]
    n = n + 1
    m = m + 1
    m = (m + 1) % 3  # Automatically set G, R, B planes
    kl = (kl + 1) % len(key)

cv2.imwrite("encrypted_img.jpg", x)
os.startfile("encrypted_img.jpg")
print("Data Hiding in Image completed successfully.")

# Prompt user to extract data
choice = input("Enter 1 to extract data from the image: ")
if choice == "1":
    # Re-enter the key to extract the text
    key = input("Re-enter the key to extract the text: ")

    decoded_text = ""
    kl = 0
    n = 0
    m = 0
    for i in range(l):
        decoded_char = c[x[n, m, z] ^ d[key[kl]]]
        decoded_text += decoded_char
        n = n + 1
        m = m + 1
        m = (m + 1) % 3  # Automatically set G, R, B planes
        kl = (kl + 1) % len(key)

    print("Encrypted text was the data hidden:", decoded_text)
else:
    print("Exiting without extracting data.")







