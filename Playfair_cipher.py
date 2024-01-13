def playfair_cipher_encrypt(plaintext, key):
    # Define the alphabet, excluding 'j'
    alphabet = 'abcdefghiklmnopqrstuvwxyz'
    
    # Remove whitespace and 'j' from the key and convert to lowercase
    key = key.lower().replace(' ', '').replace('j', 'i')
    
    # Construct the key square
    key_square = ''
    for letter in key + alphabet:
        if letter not in key_square:
            key_square += letter
    
    # Split the plaintext into digraphs, padding with 'x' if necessary
    plaintext = plaintext.lower().replace(' ', '').replace('j', 'i')
    if len(plaintext) % 2 == 1:
        plaintext += 'x'
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    
    # Define the encryption function
    def encrypt(digraph):
        a, b = digraph
        row_a, col_a = divmod(key_square.index(a), 5)
        row_b, col_b = divmod(key_square.index(b), 5)
        if row_a == row_b:
            col_a = (col_a + 1) % 5
            col_b = (col_b + 1) % 5
        elif col_a == col_b:
            row_a = (row_a + 1) % 5
            row_b = (row_b + 1) % 5
        else:
            col_a, col_b = col_b, col_a
        return key_square[row_a*5 + col_a] + key_square[row_b*5 + col_b]
    
    # Encrypt the plaintext
    encrypted_text = ''
    for digraph in digraphs:
        encrypted_text += encrypt(digraph)
    
    # Return the result
    return encrypted_text

if __name__ == "__main__":
    message = input("\tEnter the message: ")
    key = input("\tEnter the key: ")

    encrypted_message = playfair_cipher_encrypt(message, key)
    print("\n\tEncrypted message:", encrypted_message)
