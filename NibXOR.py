def encrypt_nibble_xor(text):
    """Encrypt text using nibble XOR + byte recombination."""
    binary = [format(ord(char), '08b') for char in text]
    results = []

    for bits in binary:
        middle = bits[2:6]
        outer = bits[0:2] + bits[6:8]
        xored = int(middle, 2) ^ int(outer, 2)
        results.append(format(xored, '04b'))

    # Combine nibbles into bytes
    if len(results) % 2 != 0:
        results.append('0000')  # pad last nibble
    bytelist = []
    for i in range(0, len(results), 2):
        bytelist.append(results[i] + results[i + 1])

    # Convert binary bytes to string
    return ''.join(chr(int(b, 2)) for b in bytelist)

def decrypt_nibble_xor(ciphertext):
    """Decrypt text previously encrypted with encrypt_nibble_xor."""
    binary = [format(ord(c), '08b') for c in ciphertext]
    results = []

    for b in binary:
        left, right = b[:4], b[4:]
        results.extend([left, right])

    decrypted_chars = []
    for nib in results:
        outer = nib[:2] + nib[2:]  # For symmetry, we reverse the original XOR
        middle_xor = int(nib, 2)
        middle = middle_xor ^ int(nib[:2] + nib[2:], 2)
        decrypted_chars.append(chr(int(nib[:2] + format(middle, '04b') + nib[2:], 2)))

    return ''.join(decrypted_chars).rstrip('\x00')  # Remove padding if present
