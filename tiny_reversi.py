##include <stdio.h>
#
# // map[90] = {0}
# // 盤状態:横9*縦10 y*9+xと使う。0行目と9行目は番兵
#
# // dir[]={-10, -9, -8, -1, 1, 8, 9, 10};
# // 盤を走査する場合、縦横斜め方向に向かうために足されるべき数
#int put, turn, all, done, pass, count, value, i,
#    map[90] = {0}, dir[]={-10, -9, -8, -1, 1, 8, 9, 10};

index = 0
move = 0
turn = 0
mobility = 0
flip = 0
is_pass = 0
board = [0] * 91
directions = [-10, -9, -8, -1, 1, 8, 9, 10]

#
#void check()
#{
def check():
    global move, turn, mobility, flip, index
#    if (map[put] == 0)
    if board[move] == 0:
#        for (i=0; i<8; i++) {
        for i in range(8):
            index = i
#            // 8方向走査
#            // dir[i]の方向の相手のコマの数を確認
#            for (count = 0, value = put+dir[i];
#                 map[value] == 3-turn; value += dir[i])
#                count++;
            count = 0
            value = move + directions[i]
            while board[value] == 3 - turn:
                count += 1
                value += directions[i]
#
#            if (count && map[value] == turn) {
            if count and board[value] == turn:
#                // 1枚以上存在し、その上端が自分のコマなら
#                all += count;
#                value  = put;
                mobility += count
                value = move
#
#                // doneがtrueの場合は、実際にひっくり返す
#                if (done)
                if flip:
#                    do
#                        map[value] = turn, value += dir[i];
#                    while (map[value] != turn);
                    board[value] = turn
                    value += directions[i];
                    while board[value] != turn:
                        board[value] = turn
                        value += directions[i];
#            }
#        }
#}
#
# // mapに対応するオセロ駒＆改行
#char *h=" - o x\n";
h = " - o x\n"

#
#int main()
if __name__ == '__main__':
#{
#    // 0:コマ無し
#    // 1:1player
#    // 2:2player
#    // 3:改行
#    for(i=1, map[41] = map[49] = 2; i<10; map[i++*9] = 3)
#        map[40] = map[50] = turn = pass = 1;
#
    board[41] = 2
    board[49] = 2
    for i in range(1, 10):
        board[i*9] = 3
        board[40] = 1
        board[50] = 1
        turn = 1
        is_pass = 1

#    for (;; all = done = 0) { // 毎回allとdoneを初期化
    while True:
        mobility = 0
        flip = 0

#        // 盤の表示
#        for(put = 9; put<82; ++put)
#            check(), printf("%.2s",&h[map[put]*2]);
#
        for i in range(9, 82):
            move = i
            check()
            display = board[move] * 2
            print(h[display:display+2], end="")
            move += 1

#        if(all)
        if mobility:

#            // 1枚でも駒が置けた場合はcomは左上から走査
#            // 置けた(=allの値が変わった)らturn終了
#            for(done = all = pass = put = 8; all==8; check())
#                turn - 2 ? (scanf("%d %d",&put,&i), put+=i*9): ++put;
            flip = 8
            mobility = 8
            is_pass = 8
            move = 8
            while mobility == 8:
                if turn == 2:
                    # (user)
                    move, index = [int(i) for i in input().split()]
                    move += index * 9

                    # (com)
                    #move += 1
                else:
                    move += 1
                check()
#
#        else if(pass)
#            // 駒は置けない
#            pass=0,printf("pass");
        elif is_pass:
            is_pass = 0
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
