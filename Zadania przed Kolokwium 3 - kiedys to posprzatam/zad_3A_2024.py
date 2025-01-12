"""
Zadanie 3A, 2024-01-18
Dany jest ciąg 𝑁 liczb naturalnych, z których wybieramy spójny fragment o długości 𝐾 (1 < 𝐾 < 𝑁).
Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania albo
mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić
dwa jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który
pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą, taką że stosunek tej liczby pierwszej
do długości znalezionego fragmentu jest największy. Proszę napisać funkcję find_max(T), która dla
ciągu zawartego w tablicy T, wyznaczy wartość maksymalnego ilorazu jaki można znaleźć. Jeżeli taki
podciąg nie istnieje funkcja powinna zwrócić wartość zero.
Na przykład dla ciągu: 7, 8, 6, 4, 7, 3 funkcja powinna zwrócić wartość 16.6.
Możliwe podciągi dające liczby pierwsze to:
7 + (8 ⋅ 6) + 4 = 59, 59/4 = 14.75
7 + 8 ⋅ 6 + 4 ∗ 7 = 83, 83/5 = 16.6
6 ⋅ 4 + 7 = 31, 31/3 = 10.(3)
4 + 7 = 11, 11/2 = 5.5
Uwagi:
• Czas na rozwiązanie zadania: 25 min.
• Oceniane będą: czytelność (komentarze), poprawność, efektywność rozwiązań.
• Nie wolno używać wbudowanej funkcji eval, można stosować mechanizm slicing-u
"""
from math import sqrt


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


def find_max(T):
    n = len(T)
    result = 0
    for i in range(n):
        for j in range(i+2, n+1):
            if i == 0 and j == n:
                continue
            # print(T[i:j], j-i)
            result = max(result, create_variations(j-i, T[i:j]))
    return result


def create_variations(k, T):
    result_add_first = 0
    result_multiply_first = 0
    # dodawanie first
    result = T[0]
    for i in range(1, k):
        if i % 2 == 0:
            result += T[i-1] * T[i]

    if k % 2 == 0:
        result += T[k-1]

    if is_prime(result):
        result_add_first = result/k

    # mnożenie first
    result = 0
    for i in range(k):
        if i % 2 == 1:
            result += T[i-1] * T[i]

    if k % 2 == 1:
        result += T[k-1]

    if is_prime(result):
        result_multiply_first = result/k

    return max(result_add_first, result_multiply_first)


T = [7, 8, 6, 4, 7, 3]

print(find_max(T))
