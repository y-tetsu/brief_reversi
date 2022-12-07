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
def check(board, move, turn, flip=False):
    directions = [-10, -9, -8, -1, 1, 8, 9, 10]
#    if (map[put] == 0)
    can_move = False
    if board[move] == 0:
#        for (i=0; i<8; i++) {
        for i in range(8):
#            // 8方向走査
#            // dir[i]の方向の相手のコマの数を確認
#            for (count = 0, value = put+dir[i];
#                 map[value] == 3-turn; value += dir[i])
#                count++;
            count = value = move + directions[i]
            while board[value] == 3 - turn:
                value += directions[i]
#
#            if (count && map[value] == turn) {
            if count != value and board[value] == turn:
#                // 1枚以上存在し、その上端が自分のコマなら
#                all += count;
#                value  = put;
                can_move = True
                value = move
#
#                // doneがtrueの場合は、実際にひっくり返す
#                if (done)
                if flip:
#                    do
#                        map[value] = turn, value += dir[i];
#                    while (map[value] != turn);
                    while True:
                        board[value] = turn
                        value += directions[i];
                        if board[value] == turn:
                            break
#            }
#        }
    return can_move
#}
#
# // mapに対応するオセロ駒＆改行
#char *h=" - o x\n";

#
#int main()
def reversi(debug=False):
    disc = " - o x\n"
    board = [0] * 91
    turn = 1
#{
#    // 0:コマ無し
#    // 1:1player
#    // 2:2player
#    // 3:改行
#    for(i=1, map[41] = map[49] = 2; i<10; map[i++*9] = 3)
#        map[40] = map[50] = turn = pass = 1;
#
    board[40] = board[50] = 1
    board[41] = board[49] = 2
    for i in range(1, 10):
        board[i*9] = 3

#    for (;; all = done = 0) { // 毎回allとdoneを初期化
    while True:
        can_move = False
#        // 盤の表示
#        for(put = 9; put<82; ++put)
#            check(), printf("%.2s",&h[map[put]*2]);
#
        for i in range(9, 82):
            if check(board, i, turn, False):
                can_move = no_pass = True
            display = board[i] * 2
            print(disc[display:display+2], end="")

#        if(all)
        if can_move:

#            // 1枚でも駒が置けた場合はcomは左上から走査
#            // 置けた(=allの値が変わった)らturn終了
#            for(done = all = pass = put = 8; all==8; check())
#                turn - 2 ? (scanf("%d %d",&put,&i), put+=i*9): ++put;
            move = 8
            while True:
                if turn == 2:
                    if debug:
                        move += 1
                    else:
                        x, y = [int(i) for i in input().split()]
                        move = x + y * 9
                else:
                    move += 1
                if check(board, move, turn, True):
                    break
#
#        else if(pass)
#            // 駒は置けない
#            pass=0,printf("pass");
        elif no_pass:
            no_pass = False
            print("pass")

#        else
#            // 両者とも駒を置けないので終了
#            break;
        else:
            break

#        // turn交代
#        turn = 3 - turn;
        turn = 3 - turn

#    }
#    return 0;
#}
    return board


if __name__ == '__main__':
    reversi()
