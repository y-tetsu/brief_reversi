class BriefReversi:
    def __init__(self):
        self.dirs = [-10, -9, -8, -1, 1, 8, 9, 10]
        self.discs = " - o x\n"
        self.board = [0] * 91
        self.board[40] = self.board[50] = 1
        self.board[41] = self.board[49] = 2
        self.board[9:90:9] = [3] * 9

    def start(self, turn=1, com1=True, com2=False):
        end = False
        while not (move := 0):
            for i in range(9, 82):
                if self._check(self.board, i, turn, flip=False) and not move:
                    move = i
                print(self.discs[self.board[i]*2:][:2], end="")
            if move:
                while not (end := False):
                    if not com1 and turn == 1 or not com2 and turn == 2:
                        x, y = [int(i) for i in input().split()]
                        move = x + y * 9
                    if self._check(self.board, move, turn, flip=True):
                        break
            else:
                if end:
                    break
                end = True
                print("pass")
            turn = 3 - turn

    def _check(self, board, move, turn, flip=False):
        can_move = False
        if not board[move]:
            for i in range(8):
                count = value = move + self.dirs[i]
                while board[value] == 3 - turn:
                    value += self.dirs[i]
                if count != value and board[value] == turn:
                    value = can_move = move
                    while flip:
                        board[value] = turn
                        value += self.dirs[i]
                        if board[value] == turn:
                            break
        return can_move


if __name__ == '__main__':
    BriefReversi().start()
