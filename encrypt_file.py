import argparse
import base64
import sys

from genkey import generakey
from keys import decode_key
from new import caesar_encrypt_variable

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Encrypt a file using Caesar cipher.')
    parser.add_argument('--input', type=str, default='plaintext.txt', help='Input filename (default: plaintext.txt)')
    parser.add_argument('--output', type=str, help='Output filename (default: encrypted_<input_filename>)')
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output if args.output else 'encrypted_' + input_file

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

    # read input file
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            plaintext = f.read()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        sys.exit(1)
    except Exception as exc:
        print(f"Error reading {input_file}: {exc}")
        sys.exit(1)

    # encrypt text
    try:
        ciphertext = caesar_encrypt_variable(plaintext, key_list)
    except Exception as exc:
        print(f"Error during encryption: {exc}")
        sys.exit(1)

    # optionally encode ciphertext to base64 string if user wants text output
    # (base64 adds ~33% size overhead). otherwise write raw bytes below.
    
    # write to output file as raw bytes
    try:
        raw_bytes = ciphertext.encode("utf-8")
    except Exception as exc:
        print(f"Error encoding ciphertext to bytes: {exc}")
        sys.exit(1)

    try:
        # open in binary mode to avoid any encoding/line-ending changes
        with open(output_file, "wb") as f:
            f.write(raw_bytes)
    except Exception as exc:
        print(f"Error writing {output_file}: {exc}")
        sys.exit(1)

    print(f"Encryption complete. Output saved to {output_file}")


if __name__ == "__main__":
    main()
