import os

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.upper()
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            if not is_upper:
                shifted_char = shifted_char.lower()
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)

if __name__ == "__main__":
    message = input("\tEnter the message: ")
    shift_value = int(input("\tEnter the Key value: "))

    encrypted_message = caesar_cipher(message, shift_value)
    decrypted_message = caesar_decipher(encrypted_message, shift_value)

    print("\n\tEncrypted message:", encrypted_message)
    print("\tDecrypted message:", decrypted_message) 
