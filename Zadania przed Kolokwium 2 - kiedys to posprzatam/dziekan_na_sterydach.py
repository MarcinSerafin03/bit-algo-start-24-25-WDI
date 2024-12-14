def is_correct_kings(kings, x, y):
    if y == 0:
        return True
    if y == 1:
        return abs(kings[0] - x) > 2
    return min(abs(kings[y-1] - x), abs(kings[y-2] - x)) > 2


def hetmany_ale_króle(T):
    def rek(index, value_sum):
        nonlocal T, kings, N, flag
        if index == N:
            if value_sum == 0:
                flag = True
            return

        for i in range(N):
            if is_correct_kings(kings, i, index):
                kings[index] = i
                rek(index+1, value_sum + T[index][i])
                kings[index] = -3

    flag = False
    N = len(T)
    kings = [-3 for _ in range(N)]
    rek(0, 0)
    return flag


T = [
    [1, 100, 100, 100, 100, 100, 100],
    [100, 100, 100, 2, 100, 100, 100],
    [100, 100, 100, 100, 100, 100, 3],
    [-1, 100, 100, 100, 100, 100, 100],
    [100, 100, 100, -1, 100, 100, 100],
    [100, 100, 100, 100, 100, 100, -1],
    [-3, 100, 100, 100, 100, 100, 100],
]

print(hetmany_ale_króle(T))
