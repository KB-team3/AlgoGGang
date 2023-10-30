import sys
input = sys.stdin.readline


def sudoku(ci, cj, k):  
	# ci: 행, cj: 열, k: 가능한 최소 값
    ex = [x for x in range(k)]
    for x in range(9):
        ex.append(board[ci][x])
        ex.append(board[x][cj])

    xx, yy = ci // 3 * 3, cj // 3 * 3
    for x in range(3):
        for y in range(3):
            ex.append(board[xx + x][yy + y])

    for x in range(k, 10):
        if x not in ex:
            return x
          
    return -1

board = []
blanks = []
for i in range(9):
    row = list(map(int, list(input().rstrip())))
    board.append(row)

# 채워야 하는 값들 인덱스 저장
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append([i, j])

i = 0

while 0 <= i < len(blanks):
    ni, nj = blanks[i][0], blanks[i][1]
    cur = board[ni][nj]
    res = sudoku(ni, nj, cur)
    if res == -1:
        board[ni][nj] = 0
        i -= 1
    else:
        board[ni][nj] = res
        i += 1

for i in range(9):
    ans = ''
    for ii in board[i]:
        ans += str(ii)
    print(ans)
