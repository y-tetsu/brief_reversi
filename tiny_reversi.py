DIRECTIONS = [-10, -9, -8, -1, 1, 8, 9, 10]
DISCS = " - o x\n"


def check(board, move, turn, flip=False):
    can_move = False
    if not board[move]:
        for i in range(8):
            count = value = move + DIRECTIONS[i]
            while board[value] == 3 - turn:
                value += DIRECTIONS[i]
            if count != value and board[value] == turn:
                value = can_move = move
                while flip:
                    board[value] = turn
                    value += DIRECTIONS[i]
                    if board[value] == turn:
                        break
    return can_move


def reversi(board, turn=1, com1=True, com2=False):
    end = False
    while not (move := 0):
        for i in range(9, 82):
            if check(board, i, turn, False) and not move:
                move = i
            print(DISCS[board[i]*2:][:2], end="")
        if move:
            while not (end := False):
                if not com1 and turn == 1 or not com2 and turn == 2:
                    x, y = [int(i) for i in input().split()]
                    move = x + y * 9
                if check(board, move, turn, True):
                    break
        else:
            if end:
                break
            end = True
            print("pass")
        turn = 3 - turn
    return board


if __name__ == '__main__':
    board = [0] * 91
    board[40] = board[50] = 1
    board[41] = board[49] = 2
    for i in range(1, 10):
        board[i*9] = 3
    reversi(board)
