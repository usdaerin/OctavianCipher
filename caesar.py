def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        # Shift all printable ASCII characters (from 32 to 126)
        if 32 <= ord(char) <= 126:
            shifted = chr((ord(char) - 32 + shift) % 95 + 32)
            result += shifted
        else:
            # Leave non-printable characters unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Encrypt or Decrypt (e/d): ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    if choice == 'e':
        print("Encrypted:", caesar_encrypt(text, shift))
    elif choice == 'd':
        print("Decrypted:", caesar_decrypt(text, shift))
    else:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
