def gold(T):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]

    def recursion(index, balance):
        nonlocal primes, T, n

        if index == n:
            return balance == 0

        adasie = False

        for i in range(-2, 3):
            if (T[index] - i) in primes:
                adasie = adasie or recursion(index + 1, balance - i)

        return adasie

    n = len(T)

    return recursion(0, 0)


print(gold([4, 18, 15, 14, 14, 6]))

print(gold([2, 19, 17, 13, 13, 7]))

print(gold([3, 10, 11, 18, 16, 16]))
