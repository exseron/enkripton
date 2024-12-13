import hashlib
import datetime


def decrypt_message(message, key):
    # Decrypt the message by applying the same XOR operation
    decrypted = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(message, key))
    return decrypted

# Ask the user for the encrypted message and key to decrypt
print("\nNow, let's decrypt a message.")
message = input("Enter the message you want to decrypt: ")
key_input = input("Enter the key: ")

# Decrypt the message using the provided encrypted message and key
decrypted_message = decrypt_message(message, key_input[:len(message)])
print("Decrypted Message:", decrypted_message)