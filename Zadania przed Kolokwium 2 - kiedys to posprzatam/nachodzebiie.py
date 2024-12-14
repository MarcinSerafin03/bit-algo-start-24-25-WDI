# Credit Adam Rassem


def solve(t1, t2):
    sizet1 = len(t1)
    sizet2 = len(t2)
    for row_move in range(-sizet1+1, sizet2):
        for col_move in range(-sizet1+1, sizet2):
            checked = 0
            correct5 = 0
            for i in range(sizet1):
                for j in range(sizet1):
                    if i+row_move >= 0 and i+row_move < sizet2 and j+row_move >= 0 and j+col_move < sizet2:
                        checked += 1
                        correct5 += is5correct(t1[i][j],
                                               t2[i+row_move][j+col_move])

            if checked > 0 and correct5/checked >= 0.33:
                return True
    return False


def is5correct(num1, num2):
    parz1 = 0
    parz2 = 0
    while num1 != 0:
        parz1 += 1-(num1 % 5) % 2
        num1 = num1//5
    while num2 != 0:
        parz2 += 1-(num2 % 5) % 2
        num2 //= 5
    return 1 if parz1 == parz2 else 0
