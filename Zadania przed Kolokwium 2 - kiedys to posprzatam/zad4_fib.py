def return_to_fib(num1, num2):
    a, b = 1, 1
    while a <= num1 and a <= num2:
        if a == num1 and b == num2:
            return True
        a, b = b, a+b
    return False


def check_fib(num1, num2, num3):
    if num3 - num2 == num1 and return_to_fib(num1, num2):
        return 1
    if num1 - num2 == num3 and return_to_fib(num1, num2):
        return 2
    return 0


def find(T):
    N = len(T)

    for i in range(N):
        for j in range(N):
            if i >= 2:
                check = check_fib(T[j][i-2], T[j][i-1], T[j][i])
                if check == 1:
                    result_table = [None for _ in range(N)]
                    result_table[0], result_table[1] = T[j][i-2], T[j][i-1]
                    a, b = T[j][i-1], T[j][i]
                    index = i
                    result_index = 2
                    while index < N and b != T[j][index]:
                        result_table[result_index] = b
                        result_index += 1
                        a, b = b, a+b
                    return result_table[:result_index]
                elif check == 2:
                    result_table = [None for _ in range(N)]
                    result_table[0], result_table[1] = T[j][i-2], T[j][i-1]
                    a, b = T[j][i-1], T[j][i]
                    index = i
                    result_index = 2
                    while index < N and b != T[j][index]:
                        result_table[result_index] = b
                        result_index += 1
                        a, b = b, a-b
                    return result_table[:result_index]
            if j >= 2:
                check = check_fib(T[j-2][i], T[j-1][i], T[j][i])
                if check == 1:
                    result_table = [None for _ in range(N)]
                    result_table[0], result_table[1] = T[j-2][i], T[j-1][i]
                    a, b = T[j-1][i], T[j][i]
                    index = j
                    result_index = 2
                    while index < N and b != T[index][i]:
                        result_table[result_index] = b
                        result_index += 1
                        a, b = b, a+b
                    return result_table[:result_index]
                elif check == 2:
                    result_table = [None for _ in range(N)]
                    result_table[0], result_table[1] = T[j-2][i], T[j-1][i]
                    a, b = T[j-1][i], T[j][i]
                    index = j
                    result_index = 2
                    while index < N and b != T[index][i]:
                        result_table[result_index] = b
                        result_index += 1
                        a, b = b, a-b
                    return result_table[:result_index]
