import hashlib
import datetime

# The thing is getting the exact time to use it as key for encrpytion.
timestamp = str(datetime.datetime.now())
print("Current Timestamp:", timestamp)

# Creating a SHA256 hash of the timestamp -> key process.
key = hashlib.sha256(timestamp.encode()).hexdigest()
print("Generated Key:", key)

def encrypt_message(message, key):
    encrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key))
    return encrypted

message = input("Enter the message you want to encrypt: ")

encrypted_message = encrypt_message(message, key[:len(message)])  # Use the first N chars of the key
print("Encrypted Message:", encrypted_message)
print(".")