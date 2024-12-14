def napraw(ogrod):
    def move(ogrod, x, y, d):
        new_d = d
        if ogrod[y][x] == "/":
            new_d = (-1*d[1], -1*d[0])
        if ogrod[y][x] == "\\":
            new_d = (d[1], d[0])
        return x + new_d[0], y + new_d[1], new_d

    def recurion(T, swap_ammount, changes, x, y, d):
        nonlocal result
        if swap_ammount > 2:
            return
        N = len(T)

        while x != N-1 or y != N:

            if x < 0 or x >= N or y < 0 or y >= N:
                break

            if T[y][x] == "/":
                new_T = [[T[j][i] for i in range(N)] for j in range(N)]
                new_T[y][x] = "\\"
                new_changes = [changes[i] for i in range(len(changes))]
                new_changes[swap_ammount] = (x, y)
                new_x, new_y, new_d = move(new_T, x, y, d)
                recurion(new_T, swap_ammount + 1,
                         new_changes, new_x, new_y, new_d)
            elif T[y][x] == "\\":
                new_T = [[T[j][i] for i in range(N)] for j in range(N)]
                new_T[y][x] = "/"
                new_changes = [changes[i] for i in range(len(changes))]
                new_changes[swap_ammount] = (x, y)
                new_x, new_y, new_d = move(new_T, x, y, d)
                recurion(new_T, swap_ammount + 1,
                         new_changes, new_x, new_y, new_d)

            x, y, d = move(T, x, y, d)

        if x == N-1 and y == N:
            result = changes

    result = None
    recurion(ogrod, 0, [None, None, None], 0, 0, (0, 1))
    return result[:-1]


n = 5
tab = [[" " for i in range(n)] for _ in range(n)]
tab[1][3] = tab[1][1] = tab[3][3] = tab[4][1] = "/"

tab[3][0] = tab[4][4] = "\\"

print(*tab, sep="\n")


print(napraw(tab))
