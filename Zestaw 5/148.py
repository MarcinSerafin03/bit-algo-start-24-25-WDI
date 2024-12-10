'''
https://pl.wikipedia.org/wiki/Problem_ośmiu_hetmanów
'''


def solve_8_queens_problem():
    # czy wcześniejszy hetman nie szachuje
    def is_safe(row, col):
        nonlocal board
        # wszystkie w tym samym wierszu (w kolumnie nie musimy sprawdzac bo insertujemy dokładnie 1 hetmana w 1 kolumne)
        for x in range(col):
            if board[row][x]:
                return False

        # skos w lewo i w góre
        x, y = col, row
        while x >= 0 and y >= 0:
            if board[y][x]:
                return False
            x -= 1
            y -= 1

        # skos w lewo i w dół
        x, y = col, row
        while x >= 0 and y < 8:
            if board[y][x]:
                return False
            x -= 1
            y += 1

        return True

    def print_board(N=8):
        '''
        magia (a raczej mądre używanie asci)
        NIE TRZEBA UMIEĆ TO JAKO FUN FACT JEST :)
        https://en.wikipedia.org/wiki/Box-drawing_characters
        '''
        nonlocal board, num_of_correct_boards
        num_of_correct_boards += 1
        print(f"Board number {num_of_correct_boards} found")

        gen_string = "┌"
        for i in range(N):
            gen_string += "─┬"
        gen_string = gen_string[:-1] + "┐"
        print(gen_string)

        for y in range(N):
            gen_string = "│"
            for x in range(N):
                if board[y][x]:
                    gen_string += "H│"
                else:
                    gen_string += " │"
            print(gen_string)
            if y != N-1:
                gen_string = "├"
                for x in range(N):
                    gen_string += "─┼"
                gen_string = gen_string[:-1] + "┤"
                print(gen_string)

        gen_string = "└"
        for i in range(N):
            gen_string += "─┴"
        gen_string = gen_string[:-1] + "┘"
        print(gen_string)

    # rekurencyjne wstawianie hetmanów
    def solve(column):
        nonlocal board, num_of_correct_boards
        if column == 8:
            print_board()
            return

        for i in range(8):
            if is_safe(i, column):
                board[i][column] = True
                solve(column + 1)
                board[i][column] = False

    board = [[False for _ in range(8)] for _ in range(8)]
    num_of_correct_boards = 0

    solve(0)


solve_8_queens_problem()
