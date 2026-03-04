import base64
from genkey import generakey

plaintext = "This is a test message. there has been a horrible travisty in the seventh sector, in wwhich the entire population has been turned into mutants. we need to get in there and fix this mess. there has been reports of vong forces in the area. we need to get in there and fix this mess. there has been reports of vong forces in the area"
binplain = [format(ord(char), '08b') for char in plaintext]
keyin = generakey()
keyout = [format(ord(char), '08b') for char in keyin]

def key_XOR(keyout, binplain):
    results = []
    for kbits, pbits in zip(keyout, binplain):
        # split nibbles
        kx1, kx2, kx3 = kbits[0:2], kbits[2:6], kbits[6:8]
        px1, px2, px3 = pbits[0:2], pbits[2:6], pbits[6:8]

        # per-nibble XOR
        res1 = int(px1, 2) ^ int(kx1, 2)
        res2 = int(px2, 2) ^ int(kx2, 2)
        res3 = int(px3, 2) ^ int(kx3, 2)

        # recombine into single byte
        encrypted_byte = (res1 << 6) | (res2 << 2) | res3
        results.append(format(encrypted_byte, '08b'))

    # convert results to bytes and Base64
    new_bytes = bytes(int(b, 2) for b in results)
    new_bytes_b64 = base64.b64encode(new_bytes).decode('ascii')
    return results, new_bytes, new_bytes_b64


def key_XOR_decrypt(keyout, encrypted_bytes_b64):
    # Decode Base64 to bytes
    encrypted_bytes = base64.b64decode(encrypted_bytes_b64)
    results = [format(b, '08b') for b in encrypted_bytes]
    
    plaintext_bits = []
    for kbits, ebits in zip(keyout, results):
        # split key nibbles
        kx1, kx2, kx3 = kbits[0:2], kbits[2:6], kbits[6:8]
        
        # split encrypted byte into the same nibble sizes
        res1 = int(ebits[0:2], 2)
        res2 = int(ebits[2:6], 2)
        res3 = int(ebits[6:8], 2)
        
        # XOR each nibble with key nibble to recover plaintext nibble
        px1 = res1 ^ int(kx1, 2)
        px2 = res2 ^ int(kx2, 2)
        px3 = res3 ^ int(kx3, 2)
        
        # recombine into plaintext byte
        plaintext_byte = (px1 << 6) | (px2 << 2) | px3
        plaintext_bits.append(format(plaintext_byte, '08b'))
    
    # Convert bits to ASCII string
    plaintext = ''.join(chr(int(b, 2)) for b in plaintext_bits)
    return plaintext

print("Original Plaintext:", plaintext)
encrypted_bits, encrypted_bytes, encrypted_b64 = key_XOR(keyout, binplain)
print("Encrypted (Base64):", encrypted_b64)
decrypted_text = key_XOR_decrypt(keyout, encrypted_b64)
print("Decrypted Plaintext:", decrypted_text)