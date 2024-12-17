from math import log10

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def divide(N):
    def rek(n, count):
        if n == 0:
            return is_prime(count)

        divisor = 10
        while divisor <= n * 10:
            segment = n % divisor
            if is_prime(segment):
                if rek(n // divisor, count + 1):
                    return True
            divisor *= 10

        return False

    return rek(N, 0)


print(divide(2222))


print(divide(2347))
            