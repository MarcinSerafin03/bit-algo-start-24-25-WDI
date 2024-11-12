def fibonacci(a, b, n):
    while a < n:
        a, b = b, a + b
    return a == n


def zad3():
    for suma in range(1, 2024):
        a = 0
        b = suma
        while a <= b:
            if fibonacci(a, b, 2024):
                return a, b
            a += 1
            b -= 1
    return False

print(zad3())
