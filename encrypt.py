import base64
import random
from keys import decode_key
from new import caesar_encrypt_variable


x=input("Enter the encoded key: ")
decoded_key = decode_key(x)
plaintext = input("Enter plaintext: ")
ciphertext = caesar_encrypt_variable(plaintext, decoded_key)
b64_encoded = base64.b64encode(ciphertext.encode('ascii')).decode('ascii')
print("Encrypted (base64):", b64_encoded)