#wytłumaczenie w pliku netwon_sqrt.py
#wzór minimalnie inny

def newton_cuberoot(n, epsilon=1e-10):
    x = n/2

    while True:
        next_x = x - (x**3 - n)/(3*x**2)

        if abs(next_x - x) < epsilon:
            break

        x = next_x

    return x

def test(n): #test (nie część zadania, ale ładnie ilustruje poprawność)
    for i in range(2, n+1):
        print(f"Netwon_cuberoot cubed: {newton_cuberoot(i)**3}, i: {i}")


test(40)