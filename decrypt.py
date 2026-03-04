import base64
import random
from keys import decode_key
from new import caesar_decrypt_variable

x = input("Enter the encoded key: ")
decoded_key = decode_key(x)
ciphertext = input("Enter ciphertext (base64): ")
decoded_ciphertext = base64.b64decode(ciphertext).decode('ascii')
plaintext = caesar_decrypt_variable(decoded_ciphertext, decoded_key)
print("Decrypted plaintext:", plaintext)