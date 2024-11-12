from math import log10


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_palindrome(n):
    temp = 0
    k = n
    while k > 0:
        temp = temp * 10 + k % 10
        k //= 10
    return temp == n


def is_super_palindrome_prime(n):
    temp = n
    while temp > 10:
        if not is_prime(temp) or not is_palindrome(temp):
            return False
        temp //= 10
        temp %= 10 ** (int(log10(temp)))
    if temp == 0 and int(log10(n) + 1) % 2 == 0:
        return True
    return is_prime(temp)


def zad44(n):
    cnt = 0
    for i in range(2, n):
        if is_prime(i) and is_super_palindrome_prime(i):
            cnt += 1
            print(i)
    return cnt


print(is_super_palindrome_prime(373929373))
