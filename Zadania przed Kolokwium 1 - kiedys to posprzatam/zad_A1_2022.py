
def check_seq(T, i, j):
    # if T[j] % T[i] != 0: -> może się psuć przez arytmentyke liczb zmiennoprzecinkowych
    #    return False
    multiplier = T[j] / T[i]

    for k in range(1, (j-i)):
        if T[i+k] * multiplier != T[j+k]:
            return False

    return True


def sequence(T):
    n = len(T)
    for i in range(n-2):
        for j in range(i+3, n):
            if j + (j-i) < n and check_seq(T, i, j):
                return i, j-1


print(sequence([2, 5, 7, 3, 2, 3, 5, 7, 6, 9, 15,
      21, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))
