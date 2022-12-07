##include <stdio.h>
#
# // map[90] = {0}
# // 盤状態:横9*縦10 y*9+xと使う。0行目と9行目は番兵
#
# // dir[]={-10, -9, -8, -1, 1, 8, 9, 10};
# // 盤を走査する場合、縦横斜め方向に向かうために足されるべき数
#int put, turn, all, done, pass, count, value, i,
#    map[90] = {0}, dir[]={-10, -9, -8, -1, 1, 8, 9, 10};
#
#void check()
#{
#    if (map[put] == 0)
#        for (i=0; i<8; i++) {
#            // 8方向走査
#            // dir[i]の方向の相手のコマの数を確認
#            for (count = 0, value = put+dir[i];
#                 map[value] == 3-turn; value += dir[i])
#                count++;
#
#            if (count && map[value] == turn) {
#                // 1枚以上存在し、その上端が自分のコマなら
#                all += count;
#                value  = put;
#
#                // doneがtrueの場合は、実際にひっくり返す
#                if (done)
#                    do
#                        map[value] = turn, value += dir[i];
#                    while (map[value] != turn);
#            }
#        }
#}
#
# // mapに対応するオセロ駒＆改行
#char *h=" - o x\n";
#
#int main()
#{
#    // 0:コマ無し
#    // 1:1player
#    // 2:2player
#    // 3:改行
#    for(i=1, map[41] = map[49] = 2; i<10; map[i++*9] = 3)
#        map[40] = map[50] = turn = pass = 1;
#
#    for (;; all = done = 0) { // 毎回allとdoneを初期化
#        // 盤の表示
#        for(put = 9; put<82; ++put)
#            check(), printf("%.2s",&h[map[put]*2]);
#
#        if(all)
#            // 1枚でも駒が置けた場合はcomは左上から走査
#            // 置けた(=allの値が変わった)らturn終了
#            for(done = all = pass = put = 8; all==8; check())
#                turn - 2 ? (scanf("%d %d",&put,&i), put+=i*9): ++put;
#
#        else if(pass)
#            // 駒は置けない
#            pass=0,printf("pass");
#        else
#            // 両者とも駒を置けないので終了
#            break;
#        // turn交代
#        turn = 3 - turn;
#    }
#    return 0;
#}
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
                can_move = True
                value = move
                while flip:
                    board[value] = turn
                    value += DIRECTIONS[i];
                    if board[value] == turn:
                        break
    return can_move


def reversi(com1=False, com2=False):
    turn = 1
    pre_pass = False
    board = [0] * 91
    board[40] = board[50] = 1
    board[41] = board[49] = 2
    for i in range(1, 10):
        board[i*9] = 3
    while True:
        move = 0
        for i in range(9, 82):
            if check(board, i, turn, False) and not move:
                move = i
            display = board[i] * 2
            print(DISCS[display:display+2], end="")
        if move:
            while not (pre_pass := False):
                if not com1 and turn == 1 or not com2 and turn == 2:
                    x, y = [int(i) for i in input().split()]
                    move = x + y * 9
                if check(board, move, turn, True):
                    break
        else:
            if pre_pass:
                break
            pre_pass = True
            print("pass")
        turn = 3 - turn
    return board


if __name__ == '__main__':
    reversi(True, False)
