def SITO(N):
    sito = [True for _ in range(N)]

    for i in range(2, N):  # do N bo jeszcze printujemy :)
        if sito[i]:
            print(i, "jest liczbą pierwszą 🤯")
            for j in range(2*i, N, i):
                sito[j] = False

    # fajny sposób na zwrócenie wszystkich wartości, które spełniają warunek
    return [i for i in range(2, N) if sito[i]]


print(SITO(6))
