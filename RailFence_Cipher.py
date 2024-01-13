def rail_fence_cipher_encrypt(plaintext, key):
    # Remove whitespace and convert to uppercase
    plaintext = plaintext.replace(" ", "").upper()
    key = int(key)

    # Create the rail fence matrix
    rail_fence = [['' for _ in range(len(plaintext))] for _ in range(key)]

    # Fill the matrix with the plaintext
    row, col = 0, 0
    direction = 1
    for char in plaintext:
        rail_fence[row][col] = char
        row += direction
        if row == key - 1 or row == 0:
            direction *= -1
        col += 1

    # Read the encrypted message from the matrix
    encrypted_text = ""
    for row in rail_fence:
        for char in row:
            if char != '':
                encrypted_text += char

    return encrypted_text

if __name__ == "__main__":
    message = input("\tEnter the message: ")
    key = input("\tEnter the key (number of rails): ")

    encrypted_message = rail_fence_cipher_encrypt(message, key)
    
    # Display the encrypted message in rows
    encrypted_rows = [encrypted_message[i:i + len(message)] for i in range(0, len(encrypted_message), len(message))]
    for row in encrypted_rows:
        print("\n\tEncrypted message:", row)
