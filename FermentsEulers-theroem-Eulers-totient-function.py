import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent //= 2
        base = (base * base) % modulus
    return result


def fermat_test(n, k=5):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if gcd(a, n) != 1:
            return False
        if power_mod(a, n - 1, n) != 1:
            return False
    return True


def euler_totient_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def euler_theorem(a, m):
    if gcd(a, m) != 1:
        return None  # Euler's theorem doesn't apply
    phi_m = euler_totient_function(m)
    return power_mod(a, phi_m, m)


print("Fermat's Theorem Test ")
n = int(input("Enter a number : "))
if fermat_test(n):
    print(f"{n} is probably prime.")
else:
    print(f"{n} is composite.")
print("\nEuler’s totient Function")
print(f"Euler's Totient Function of {n} is {euler_totient_function(n)}")
print("\nEuler Theorem")
a = int(input("Enter a base 'a' : "))
m = int(input("Enter a modulus 'm' : "))
result = euler_theorem(a, m)
if result is None:
    print("Euler's Theorem doesn't apply for the given values of 'a' and 'm'.")
else:
    print(f"Euler's Theorem: {a}^{euler_totient_function(m)} % {m} = {result}")
