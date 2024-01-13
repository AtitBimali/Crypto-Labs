def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def primitive_roots(p):
    if not is_prime(p):
        return []
    
    phi = p - 1
    factors = []
    x = phi
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            factors.append(i)
            while x % i == 0:
                x //= i
    if x > 1:
        factors.append(x)
    
    primitive_roots_list = []
    for r in range(2, p):
        is_primitive_root = True
        for factor in factors:
            if pow(r, phi // factor, p) == 1:
                is_primitive_root = False
                break
        if is_primitive_root:
            primitive_roots_list.append(r)
    
    return primitive_roots_list

def main():
    prime_number = int(input("Enter a prime number: "))
    primitive_roots_list = primitive_roots(prime_number)
    
    if len(primitive_roots_list) > 0:
        print(f"Primitive roots of {prime_number} are {primitive_roots_list}")
    else:
        print(f"{prime_number} does not have primitive roots.")
        
if __name__ == "__main__":
    main()
  