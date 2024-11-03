def create_ciąg(T, i):
    n = len(T)
    lenght = 1
    for j in range(i+1, n):
        if T[j-1] < T[j]:
            lenght += 1
        else:
            break
    if lenght > 2:
        return (i, j-1)  # indeks początkowy i indeks końcowy
    else:
        return None


def sequence(T):
    n = len(T)
    Potential_results = [None for _ in range(n)]
    curr_index = 0
    for i in range(n):
        if i == 0 or T[i] < T[i-1]:
            result = create_ciąg(T, i)
            if result is not None:
                Potential_results[curr_index] = result
                curr_index += 1

# [(0,3),(4,8),None,None,...] <- potencjalny wygląd tabeli
    i = 0
    while Potential_results[i] is not None:
        j = i + 1
        while Potential_results[j] is not None:
            if T[Potential_results[i][0]] > T[Potential_results[j][1]] or T[Potential_results[j][0]] > T[Potential_results[i][1]]:
                return True
            j += 1
        i += 1

    return False


print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))

print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]))
