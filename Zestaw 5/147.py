'''
https://pl.wikipedia.org/wiki/Wieże_Hanoi
'''
# ale ze mnie sigma ngl 🍕


def hanoi(n):
    def print_after_move():
        nonlocal A, B, C, moves
        print(f"move number {moves}")
        print(f"A = {A}")
        print(f"B = {B}")
        print(f"C = {C}")
        print("\n")

    def solve_hanoi(n, A, B, C):
        nonlocal moves
        if n > 0:
            solve_hanoi(n-1, A, C, B)
            if len(A) != 0:
                C.append(A.pop())  # używam bo moge :)
                # i działa (wcześniej nie chiało)

            moves += 1
            print_after_move()
            solve_hanoi(n-1, B, A, C)

    A = ["Krążek" + str(i) for i in range(n)]
    B = []
    C = []

    moves = 0

    solve_hanoi(n, A, B, C)

    print(moves)


hanoi(4)
