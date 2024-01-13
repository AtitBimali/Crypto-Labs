def vigenere_cipher_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_len = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shift = ord(key[i % key_len]) - 65
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            if not is_upper:
                shifted_char = shifted_char.lower()
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

if __name__ == "__main__":
    message = input("\tEnter the message: ").upper()
    key = input("\tEnter the key: ").upper()

    encrypted_message = vigenere_cipher_encrypt(message, key)
    print("\n\tEncrypted message:", encrypted_message)
