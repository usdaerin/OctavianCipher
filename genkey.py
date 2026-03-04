import base64
import random
from keys import generate_key, encode_key

def generakey():
    newkey = generate_key(length=64, min_value=1, max_value=255)
    encoded_key = encode_key(newkey)
    return encoded_key
