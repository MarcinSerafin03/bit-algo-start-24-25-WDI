def fibo(T):
    # print(T)
    a, b = 1, 1
    while a < T[0] or b < T[1]:
        a, b = b, a + b
    if a != T[0]:
        return False

    for i in range(1, len(T)):
        a, b = b, a + b
        if a != T[i]:
            return False
    return True


def find_fibo(T):
    maxi = 0
    for i in range(len(T)):
        for j in range(len(T[i]) - 2):
            if fibo(T[i][j:j + 3]):
                curr = 3
                a, b = T[i][j + 1], T[i][j + 2]
                for k in range(j + 3, len(T[i]) - 2):
                    if a + b == T[i][j + 3]:
                        curr += 1
                    else:
                        maxi = max(curr, maxi)
                maxi = max(curr, maxi)
    for j in range(len(T[0])):
        for i in range(len(T) - 2):
            column_slice = [T[i][j], T[i + 1][j], T[i + 2][j]]
            if fibo(column_slice):
                curr = 3
                a, b = T[i + 1][j], T[i + 2][j]
                for k in range(i + 3, len(T)):
                    if a + b == T[k][j]:
                        curr += 1
                        a, b = b, a + b
                    else:
                        break
                maxi = max(curr, maxi)


    return maxi


T=[[1,6,3,9],[1,4,3,6],[0,6,8,5],[3,4,6,7]]

print(find_fibo((T)))