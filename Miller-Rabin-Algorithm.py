import random


def power(x, y, p): #used for x^y % p
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2 #used for integer output since the output can be float
        x = (x * x) % p
    return result


def miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = power(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = power(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    print("\tTesting for Primality \n")
    num = int(input("Enter a number : "))
    if miller_rabin(num):
        print(f"The number {num} is likely to be prime number.")
    else:
        print(f"The number '{num}' is not a prime number.")


if __name__ == "__main__":
    main()
