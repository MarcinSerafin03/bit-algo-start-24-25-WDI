
#https://pl.wikipedia.org/wiki/Metoda_Newtona

# x = sqrt(n) | ()^2
# x^2 = n
# x^2 - n = 0 <= f(x)
# f'(x) = 2x

# x_k+1 = x_k - f(x_k)/f'(x_k) => x_k+1 = x_k - (x_k^2 - n)/(2x_k)



def newton_sqrt(n, epsilon=1e-10): #syntax sugar - wartości domyślne, dzięki temu nie trzeba ich podawać przy wywołaniu
    if n == 0: #edgecase
        return 0
    
    x = n/2

    while True: #imitacja pętli do while
        next_x = x - (x**2 - n)/(2*x)

        if abs(next_x - x) < epsilon:
            break

        x = next_x
        
    return x


def test(n): #test (nie część zadania, ale ładnie ilustruje poprawność)
    for i in range(2, n+1):
        print(f"Netwon_sqrt(i) squared: {newton_sqrt(i)**2}, i: {i}")

test(40)
