import random

# Step 1: Choose prime numbers and primitive root
prime_modulus = int(input("Enter a prime modulus (p): "))
primitive_root = int(input("Enter a primitive root (g): "))

# Step 2: Choose secret private keys for both parties
private_key_A = int(input("Enter private key for party A: "))
private_key_B = int(input("Enter private key for party B: "))

# Step 3: Calculate public keys for both parties
public_key_A = (primitive_root ** private_key_A) % prime_modulus
public_key_B = (primitive_root ** private_key_B) % prime_modulus

# Step 4: Exchange public keys

# Step 5: Calculate shared secret key for both parties
shared_secret_key_A = (public_key_B ** private_key_A) % prime_modulus
shared_secret_key_B = (public_key_A ** private_key_B) % prime_modulus

# Step 6: Verify that the shared secret keys match
if shared_secret_key_A == shared_secret_key_B:
    print("Shared secret keys match.")
    print(f"Shared Secret Key: {shared_secret_key_A}")
else:
    print("Shared secret keys do not match.")