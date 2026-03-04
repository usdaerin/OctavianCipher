import base64
import sys

from genkey import generakey
from keys import decode_key
from new import caesar_encrypt_variable


def main():
    # generate and display encoded key
    try:
        encoded_key = generakey()
    except Exception as exc:
        print(f"Error generating key: {exc}")
        sys.exit(1)

    print(f"Generated encoded key: {encoded_key}")

    # decode key
    try:
        key_list = decode_key(encoded_key)
    except Exception as exc:
        print(f"Error decoding key: {exc}")
        sys.exit(1)

    # read lorem.txt
    try:
        with open("lorem.txt", "r", encoding="utf-8") as f:
            plaintext = f.read()
    except FileNotFoundError:
        print("Error: lorem.txt not found.")
        sys.exit(1)
    except Exception as exc:
        print(f"Error reading lorem.txt: {exc}")
        sys.exit(1)

    # encrypt text
    try:
        ciphertext = caesar_encrypt_variable(plaintext, key_list)
    except Exception as exc:
        print(f"Error during encryption: {exc}")
        sys.exit(1)

    # encode ciphertext to base64 string
    try:
        b64 = base64.b64encode(ciphertext.encode("utf-8")).decode("ascii")
    except Exception as exc:
        print(f"Error encoding ciphertext to base64: {exc}")
        sys.exit(1)

    # write to encrypted_lorem.txt
    try:
        with open("encrypted_lorem.txt", "w", encoding="utf-8") as f:
            f.write(b64)
    except Exception as exc:
        print(f"Error writing encrypted_lorem.txt: {exc}")
        sys.exit(1)

    print("Encryption complete. Output saved to encrypted_lorem.txt")


if __name__ == "__main__":
    main()
