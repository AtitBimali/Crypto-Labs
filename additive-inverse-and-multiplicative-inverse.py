def find_additive_inverse(a, p):
    return (p - a) % p


def find_multiplicative_inverse(a, p):
    for i in range(1, p):
        if (a * i) % p == 1:
            return i
    return None


p = int(input("\nEnter the prime number , p: "))
a = int(input("Enter the element to find inverses For , a : "))

additive_inverse = find_additive_inverse(a, p)
multiplicative_inverse = find_multiplicative_inverse(a, p)

print(f"\n\tAdditive Inverse of {a} is ", additive_inverse)
print(f"\n\tMultiplicative Inverse of {a} is ", multiplicative_inverse)
