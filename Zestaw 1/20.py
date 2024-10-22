from math import sqrt

def An1(A,B):
    """
    :param A: An
    :param B: Bn
    :return: An+1

    Funckja zwraca wartość An+1 na podstawie An i Bn
    """
    return sqrt(A*B)

def Bn1(A,B):
    """
    :param A: An
    :param B: Bn
    :return: Bn+1

    Funckja zwraca wartość Bn+1 na podstawie An i Bn
    """
    return (A+B)/2.0

def mean(A,B):
    """
    :param A: Pierwsza liczba
    :param B: Druga Liczba
    :return: Średnia
    """
    # epsilon bo komputer nie umie w dzielenie i liczby sobie równo mogą sie rożnić na jakieś liczbie po przecinku
    eps = 1e-10
    # Przechodzimy w pętli podstawiając kolejne elementy ciągu aż liczby bedą równe czyli aż różnica między nimi będzie mniejsza niż epsilon
    while abs(A-B)>eps:
        A, B = An1(A,B), Bn1(A,B)
    return A


print(mean(15,12))