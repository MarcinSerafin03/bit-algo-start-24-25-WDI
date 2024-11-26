from math import sqrt


def is_prime(n):
    if n <= 1:  # 0, 1 lub liczby ujemne
        return False
    if n == 2 or n == 3 or n == 5:  # 2, 3, 5
        return True

    if n % 5 == 0 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 6

    for i in range(5, int(sqrt(n)) + 1, 6):
        # 5, 7, 11, 13...
        if n % i == 0 or n % (i+2) == 0:
            return False

    return True


def print_prime_components(n):
    def rek(n, power, accumulator):
        # akumulator zbiera informacje o tym co mamy
        nonlocal base_n
        # warunek końcowy
        if n == 0:
            if accumulator >= 10 and accumulator != base_n and is_prime(accumulator):
                print(accumulator)
            return

        # krok rekurencji
        rek(n // 10, power, accumulator)
        rek(n // 10, power + 1, accumulator + (n % 10) * 10 ** power)

    base_n = n
    rek(n, 0, 0)


print_prime_components(2137)
