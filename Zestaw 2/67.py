def czynniki(n):
    if n <= 1:
        return []

    czynnik = [False for _ in range(n+1)]  # na appenda jest ban

    dzielnik = 2
    while dzielnik <= n:
        if n % dzielnik == 0:
            czynnik[dzielnik] = True
        while n % dzielnik == 0:  # opcjonalne (nie trzeba przy dzielnik <= n)
            n //= dzielnik
        dzielnik += 1

    return czynnik


def czy_skok(T):
    l = len(T)
    # tabela informuje czy można skoczyć z początku do i-tego indeksu
    Czy_może_skoczyć = [False for _ in range(l)]
    Czy_może_skoczyć[0] = True

    i = 0
    while i < l:  # ewentualnie pętla for, nie ma różnicy :)
        # if Czy_może_skoczyć[i] == True to zbrodnia wojenna, nie ma co porównywac wartości bo
        # trzymamy w tablicy wartości prawda/fałsz
        if Czy_może_skoczyć[i]:
            czynnik = czynniki(T[i])
            for j in range(len(czynnik)):
                if czynnik[j] and i + j < l:  # wyjście poza tabele check
                    Czy_może_skoczyć[i + j] = True
        i += 1

    return Czy_może_skoczyć[l-1]


print(czy_skok([4, 9, 10, 3, 5, 12, 2, 11, 12, 15212512]))
