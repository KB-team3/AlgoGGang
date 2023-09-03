import sys
input = sys.stdin.readline

def roll(d, direction):
    nd = d

    if direction == 1:
        nd[3], nd[5], nd[1], nd[2] = d[2], d[3], d[5], d[1]
    elif direction == 2:
        nd[3], nd[2], nd[1], nd[5] = d[5], d[3], d[2], d[1]
    elif direction == 3:
        nd[0], nd[2], nd[4], nd[5] = d[2], d[4], d[5], d[0]
    elif direction == 4:
        nd[2], nd[4], nd[5], nd[0] = d[0], d[2], d[4], d[5]

    return nd
    

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
moves = [*map(int,input().split())]
dice = [0, 0, 0, 0, 0, 0]

# 동: 1, 서: 2, 북: 3, 남: 4
for m in moves:
    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    # 현재 좌표는 x, y로 유지하여 관리
    ni, nj = x + di[m - 1], y + dj[m - 1]

    # 범위 체크
    if 0 <= ni < N and 0 <= nj < M:
        x, y = ni, nj
        dice = roll(dice, m)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0

        print(dice[2])
