from random import randint


def rozklad(n):
    sygnatura = 1

    dzielnik = 2
    while n > 1:
        if n % dzielnik == 0:
            sygnatura *= dzielnik
        while n % dzielnik == 0:
            n //= dzielnik
        dzielnik += 1

    return sygnatura


def zgodne(T):
    n = len(T)

    for i in range(n):
        T[i] = rozklad(T[i])

    result = 0

    for i in range(n):
        for j in range(max(i-2, 0), min(i+3, n)):
            if j == i:
                continue
            if T[i] == T[j]:
                result += 1
                break

    return result


T = [randint(2, 999) for _ in range(30)]

print(f"Tablica {T} ma {zgodne(T)} liczbe elementów mających przynajmniej jednego zgodnego sąsiada")
