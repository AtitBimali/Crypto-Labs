import random

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to check if two numbers are coprime
def coprime(a, b):
    return gcd(a, b) == 1

# Function to check if a number is prime
def is_prime(p):
    if p < 2:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

# Function to calculate the modular inverse
def mod_inv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA key pairs
def generate_rsa_keys(p, q):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be prime numbers")
    if p == q:
        raise ValueError("p and q must be different")
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = random.randrange(1, phi_n)
    while not coprime(e, phi_n):
        e = random.randrange(1, phi_n)
    d = mod_inv(e, phi_n)
    return (e, n), (d, n)

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt an encrypted message
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    return decrypted_message

if __name__ == "__main__":
    p = int(input("Enter a prime number (p): "))
    q = int(input("Enter a prime number (q): "))
    
    public_key, private_key = generate_rsa_keys(p, q)
    
    message = input("Enter a message to encrypt: ")
    encrypted_message = encrypt(message, public_key)
    
    print("Encrypted message:", encrypted_message)
    
    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted message:", decrypted_message)
