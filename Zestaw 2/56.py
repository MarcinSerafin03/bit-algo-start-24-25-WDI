from math import sqrt, log10


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


def different_digits(n):
    was_digit_seen = [False for _ in range(10)]
    while n > 0:
        if was_digit_seen[n % 10] == True:
            return False
        else:
            was_digit_seen[n % 10] = True
        n //= 10

    return True


def check_correct(k, l, M, N):
    # ucinamy z lewej
    k %= 10**(l-M)

    # ucinamy z prawej
    k //= 10**N

    # print(f"found new number {k}") for debuging

    if is_prime(k) and different_digits(k):
        return k

    return 0


def zad56(k):
    if k <= 1:
        return 0

    biggest_found = 0
    l = int(log10(k)) + 1
    for M in range(l):
        for N in range(l-M):
            biggest_found = max(biggest_found, check_correct(k, l, M, N))

    return biggest_found


k = 1202742516

print(f"biggest number that is good for {k} is {zad56(k)}")
