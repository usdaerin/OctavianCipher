import base64
from caesar import caesar_encrypt, caesar_decrypt

def caesar_encrypt_variable(text, shift_list):
    # Step 1: Original keystring encryption
    n = len(shift_list)
    temp = ""
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            shifted = chr((ord(char) - 32 + shift_list[i % n]) % 95 + 32)
            temp += shifted
        else:
            temp += char

    # Step 2: Layered shifts
    result = temp
    for shift in shift_list:
        result = ''.join(
            chr((ord(c) - 32 + shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
            for c in result
        )
    total_shift = sum(shift_list)
    result = ''.join(
        chr((ord(c) - 32 + total_shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
        for c in result
    )
    return result

def caesar_decrypt_variable(text, shift_list):
    # Step 1: Reverse total shift
    total_shift = sum(shift_list)
    temp = ''.join(
        chr((ord(c) - 32 - total_shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
        for c in text
    )
    # Step 2: Reverse layered shifts (in reverse order)
    for shift in reversed(shift_list):
        temp = ''.join(
            chr((ord(c) - 32 - shift) % 95 + 32) if 32 <= ord(c) <= 126 else c
            for c in temp
        )
    # Step 3: Original keystring decryption
    n = len(shift_list)
    result = ""
    for i, char in enumerate(temp):
        if 32 <= ord(char) <= 126:
            shifted = chr((ord(char) - 32 - shift_list[i % n]) % 95 + 32)
            result += shifted
        else:
            result += char
    return result
