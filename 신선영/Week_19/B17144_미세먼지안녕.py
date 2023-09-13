import sys
input = sys.stdin.readline


def spread(board):  # 미세먼지 확산
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    plus = [[0] * C for _ in range(R)]
    minus = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            cur = board[i][j]
            if cur != 0 and cur != -1:
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != -1:
                        plus[ni][nj] += board[i][j] // 5
                        minus[i][j] += board[i][j] // 5

    for i in range(R):
        for j in range(C):
            board[i][j] += plus[i][j]
            board[i][j] -= minus[i][j]

    return board
                    
                
def clear(i1, i2):
    for i in range(i1 - 2, -1, -1):
        board[i + 1][0] = board[i][0]
    for j in range(C - 1):
        board[0][j] = board[0][j + 1]
    for i in range(1, i1 + 1):
        board[i - 1][C - 1] = board[i][C - 1]
    for j in range(C - 1, 1, -1):
        board[i1][j] = board[i1][j - 1]
    board[i1][1] = 0    
    for i in range(i2 + 1, R - 1):
        board[i][0] = board[i + 1][0]
    for j in range(1, C):
        board[R - 1][j - 1] = board[R - 1][j]
    for i in range(R - 1, i2, -1):
        board[i][C - 1] = board[i - 1][C - 1]
    for j in range(C - 1, 1, -1):
        board[i2][j] = board[i2][j - 1]
    board[i2][1] = 0
    

R, C, T = map(int, input().split())

board = [[*map(int, input().split())] for _ in range(R)]
cleaners = []

for i in range(R):  # 공기청정기는 항상 1번 열에 설치
    if board[i][0] == -1:
        cleaners.append(i)

for t in range(T):
    board = spread(board)
    clear(cleaners[0], cleaners[1])


ans = 2
for b in board:
    ans += sum(b)

print(ans)
