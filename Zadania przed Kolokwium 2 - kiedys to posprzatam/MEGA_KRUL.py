def solve():
    T = [None for _ in range(100)]
    index = 0
    while index < 5:
        position_x = int(input(f"Podaj (x) pozycje {index} króla"))
        position_y = int(input(f"Podaj (y) pozycje {index} króla"))
        T[index] = (position_x, position_y,
                    max(abs(100 - position_x), abs(100 - position_y)))
        index += 1

    for i in range(5):
        for j in range(i + 1, 5):
            if T[i][2] == T[j][2]:
                print(
                    f"Król z pozycji({T[i][0]},{T[i][1]}) jest równoodległy od środka względem króla o pozycji ({T[j][0]},{T[j][1]})")
                return
    print("nimo")


solve()
