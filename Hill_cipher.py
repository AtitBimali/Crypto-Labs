def matrix_multiply(matrix1, matrix2, mod):
    result = [[0] * len(matrix2[0]) for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
            result[i][j] %= mod
    return result

def get_key_matrix(size):
    print(f"\tEnter {size}x{size} Key Matrix:")
    key_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            element = int(input(f"\tEnter element at position ({i+1}, {j+1}): "))
            row.append(element)
        key_matrix.append(row)
    return key_matrix

def plaintext_to_numeric(text):
    return [ord(char) - 97 for char in text]

def numeric_to_ciphertext(numbers):
    return ''.join(chr(num % 26 + 65) for num in numbers)

def hill_cipher_encrypt(plaintext, key_matrix):
    size = len(key_matrix)
    mod = 26

    plaintext = plaintext.lower()
    plaintext_numbers = plaintext_to_numeric(plaintext)

    while len(plaintext_numbers) % size != 0:
        plaintext_numbers.append(23)  # Padding with 'X' (ASCII: 120) which is 23 in 0-based representation

    num_blocks = len(plaintext_numbers) // size
    plaintext_vectors = [plaintext_numbers[i:i+size] for i in range(0, len(plaintext_numbers), size)]

    if len(plaintext_vectors[0]) == size:
        encrypted_vectors = matrix_multiply(plaintext_vectors, key_matrix, mod)
    else:
        print("Error: Key Matrix size does not match plaintext vector size.")
        return None

    encrypted_text = numeric_to_ciphertext([num for vector in encrypted_vectors for num in vector])

    return encrypted_text

if __name__ == "__main__":
    message = input("\tEnter the message: ")
    size = int(input("\tEnter Key Matrix size: "))

    key_matrix = get_key_matrix(size)

    encrypted_message = hill_cipher_encrypt(message, key_matrix)
    if encrypted_message:
        print("\n\tEncrypted message:", encrypted_message)
