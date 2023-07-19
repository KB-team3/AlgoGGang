from collections import deque
M, N = map(int, input().split(" "))
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split(" ")))
queue = deque()
max_day = 0
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            queue.append([i,j,0])
while queue:
    x, y, day = queue.popleft()
    max_day = day
    for ddx, ddy in zip(dx, dy):
        tx, ty = x+ddx, y+ddy
        if 0<=tx<N and 0<=ty<M and board[tx][ty]==0:
            board[tx][ty]=1
            queue.append([tx, ty, day+1])
for i in range(N):
    if 0 in board[i]:
        print("-1")
        exit(0)
print(max_day)