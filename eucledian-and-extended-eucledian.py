def euclidean_algorithm(a, b):
    while b:
        a, b = b, a % b
    return a


def extended_euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_euclidean_algorithm(b, a % b)
        x, y = y, x - (a // b) * y
        return gcd, x, y


a = int(input("Enter a: "))
b = int(input("Enter b: "))

gcd = euclidean_algorithm(a, b)
print("\nUsing Euclidean Algorithm")
print(f"GCD({a},{b}) :", gcd)

gcd, x, y = extended_euclidean_algorithm(a, b)
print("\nUsing Extended Euclidean Algorithm")
print(f"Extended GCD({a},{b}) :", gcd)
print(f"Coefficients (S, T) for {a} , {b}: ({x}, {y})\n")
