class BriefReversi:
    def __init__(self):
        self.dirs = [-10, -9, -8, -1, 1, 8, 9, 10]
        self.discs = ' - o x\n'
        self.board = [0 if i % 9 else 3 for i in range(91)]
        self.board[40] = self.board[50] = self.turn = 1
        self.board[41] = self.board[49] = 2

    def play(self, com1=False, com2=True):
        end = False
        while not (move := 0):
            for i in range(9, 82):
                if self._check(self.board, i, flip=False) and not move:
                    move = i
                print(self.discs[self.board[i]*2:][:2], end='')
            while move and not (end := False):
                if not com1 and self.turn == 1 or not com2 and self.turn == 2:
                    x, y = [int(i) for i in input().split()]
                    move = x + y * 9
                if self._check(self.board, move, flip=True):
                    break
            else:
                if end:
                    break
                end = True
                print('pass')
            self.turn = 3 - self.turn

    def _check(self, board, move, flip=False):
        if not (ret := False) and not board[move]:
            for i in range(8):
                count = value = move + self.dirs[i]
                while board[value] == 3 - self.turn:
                    value += self.dirs[i]
                if count != value and board[value] == self.turn:
                    ret = value = move
                    while flip:
                        board[value] = self.turn
                        value += self.dirs[i]
                        if board[value] == self.turn:
                            break
        return ret


if __name__ == '__main__':
    BriefReversi().play()
