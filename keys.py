import base64
import random

def encode_key(key_list):
    # Convert list of ints to bytes, then to base64 string
    key_bytes = bytes(key_list)
    return base64.b64encode(key_bytes).decode('ascii')

def decode_key(key_str):
    # Convert base64 string back to list of ints
    key_bytes = base64.b64decode(key_str)
    return list(key_bytes)


#genreates the key randomly 
def generate_key(length=64, min_value=1, max_value=255):
    return [random.randint(min_value, max_value) for _ in range(length)]



# Example usage:
key = generate_key(length=64, min_value=1, max_value=255)
encoded = encode_key(key)
decoded = decode_key(encoded)
