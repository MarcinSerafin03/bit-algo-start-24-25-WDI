'''Zadanie 51. Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej licz-
bie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każ-
dej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby
12375,17523,75123,17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować
z dwóch zadanych liczb'''

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


def bit_mask(n, l):
    binary_digits = [0] * l

    index = l - 1
    while n > 0:
        binary_digits[index] = n % 2
        n //= 2
        index -= 1

    return binary_digits


def check_mask(mask, l1, l2):
    for el in mask:
        if el == 0:
            l1 -= 1
        else:
            l2 -= 1

    return l1 == 0 and l2 == 0


def num_to_table(n, l):
    table = [0] * l
    index = l - 1
    while n > 0:
        table[index] = n % 10
        n //= 10
        index -= 1

    return table


def zad51(n1, n2):
    l1 = int(log10(n1)) + 1
    l2 = int(log10(n2)) + 1
    l = l1 + l2
    n1_table = num_to_table(n1, l1)
    n2_table = num_to_table(n2, l2)

    result = 0

    for i in range(1, 2**l):
        mask = bit_mask(i, l)

        if not check_mask(mask, l1, l2):
            continue

        num = 0

        n1_index = 0
        n2_index = 0

        for j in range(l):
            num *= 10
            if mask[j] == 1:
                num += n2_table[n2_index]
                n2_index += 1
            else:
                num += n1_table[n1_index]
                n1_index += 1

        if is_prime(num):
            result += 1

    return result
