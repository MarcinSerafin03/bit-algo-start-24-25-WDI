# Dana jest tablica T zawierająca ciąg liczb naturalnych. Maksymalny, spójny podciąg rosnący to taki, w
# którym przed pierwszym elementem nie ma elementu mniejszego, a za ostatnim elementem nie ma elementu
# większego. Proszę napisać funkcję sequence(T) która sprawdza czy w tablicy można znaleźć dwa maksymalne, spójne podciągi rosnące, każdy o długości większej od 2, takie aby po ich złączeniu stanowiły jeden
# ciąg rosnący. Funkcja powinna zwrócić wartość True albo False
# Przykłady:
# sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2] ) zwróci True
# sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2] ) zwróci False

def sequence(T):
    first_min=float('inf')
    first_max=0
    for i in range(1,len(T)-1):
        if T[i]<first_min:
            first_min=T[i]
            break
    for i in range(1,len(T)-1):
        if T[i]>first_max:
            first_max=T[i]
            break



    return False

