def najdłuższy_ciąg_geometryczny(T):
    if len(T) <= 1:
        return len(T)  # [] (pusta tablica) => ciąg długości 0

    maksymalna_długośc = 1
    obecna_długośc = 1
    inverse = False  # czy n czy 1/n

    obecny_stosunek = None

    for i in range(1, len(T)):
        # dodatek z zajęć, po to żeby liczyć też ciągi o q = 1/n
        if T[i - 1] != 0 and (T[i] % T[i - 1] == 0 or T[i-1] % T[i] == 0):
            if T[i] % T[i - 1] == 0:
                stosunek = T[i] / T[i - 1]
                curr_inverse = False
            else:
                stosunek = T[i-1] / T[i]
                curr_inverse = True
            if obecny_stosunek == stosunek and inverse == curr_inverse:
                obecna_długośc += 1
                maksymalna_długośc = max(maksymalna_długośc, obecna_długośc)
            else:
                obecny_stosunek = stosunek
                inverse = curr_inverse
                obecna_długośc = 2
        else:
            obecny_stosunek = None
            obecna_długośc = 1
            inverse = False

    return maksymalna_długośc


T = [2, 4, 8, 16, 3, 9, 27, 81, 243, 5, 10]

print(najdłuższy_ciąg_geometryczny(T))
