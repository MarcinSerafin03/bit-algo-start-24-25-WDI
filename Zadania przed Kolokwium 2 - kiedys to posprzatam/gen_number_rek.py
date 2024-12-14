'''Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące
w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb wejściowych musi być zachowana. Na przykład mając liczby 123 i 75
możemy zbudować liczby 12375, 17523, 75123, 17253, itd. Proszę napisać funkcję która wyznaczy
ile liczb pierwszych można zbudować z dwóch zadanych liczb.'''
from math import sqrt, log10


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i < sqrt(n+1) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def build_third_number(l1, l2):
    def rek(ind_1, ind_2, acc):
        nonlocal l1, l2, n1, n2, result
        if ind_1 == n1 and ind_2 == n2:
            print(acc)
            if is_prime(acc):
                result += 1
            return

        if ind_1 != n1:
            rek(ind_1+1, ind_2, acc * 10 +
                ((l1 % (10**(n1-ind_1))) // (10**(n1-ind_1-1))))

        if ind_2 != n2:
            rek(ind_1, ind_2+1, acc * 10 +
                ((l2 % (10**(n2-ind_2))) // (10**(n2-ind_2-1))))

    n1 = int(log10(l1)) + 1
    n2 = int(log10(l2)) + 1
    result = 0
    rek(0, 0, 0)
    return result


print(build_third_number(3, 73))
