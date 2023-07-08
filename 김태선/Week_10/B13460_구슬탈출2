import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 이동할 다음 위치 계산
def move(x, y, k):
    cnt = 1
    while True:
        cnt += 1
        nx, ny = x + dx[k], y + dy[k]
        # 이동할 위치가 구멍이거나 벽이면 return
        if board[nx][ny] == 'O': return (nx, ny, cnt)
        if board[nx][ny] == '#': return (x, y, cnt - 1)
        x, y = nx, ny

# BFS
def solution(rx, ry, bx, by):
    dist = [[[[-1] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    dist[rx][ry][bx][by] = 0
    q = deque([(rx, ry, bx, by)])

    while q:
        rx, ry, bx, by = q.popleft()
        # 거리가 10 이상이면 패스
        if dist[rx][ry][bx][by] > 10: continue
        # 빨간 구슬이 구멍에 도착하면 return
        if board[rx][ry] == 'O': return dist[rx][ry][bx][by]
        for k in range(4):
            nrx, nry, nrd = move(rx, ry, k)
            nbx, nby, nbd = move(bx, by, k)
            # 파란 구슬이 구멍에 빠지면 패스
            if board[nbx][nby] == 'O': continue
            # 빨간 구슬의 다음 위치와 파란 구슬의 다음 위치가 같을 경우, 거리(nrd or nbd)가 큰 것이 더 뒤에 있던 경우임
            # 따라서 이동할 다음 위치를 한칸 뒤로 빼주는 것이 필요
            if (nrx, nry) == (nbx, nby):
                if nrd > nbd:
                    nrx -= dx[k]
                    nry -= dy[k]
                else:
                    nbx -= dx[k]
                    nby -= dy[k]
            # 방문 했으면 패스
            if dist[nrx][nry][nbx][nby] != -1: continue
            dist[nrx][nry][nbx][nby] = dist[rx][ry][bx][by] + 1
            q.append((nrx, nry, nbx, nby))
    return -1

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]

    rx, ry, bx, by = -1, -1, -1, -1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'R':
                rx, ry = i, j
            if board[i][j] == 'B':
                bx, by = i, j
    print(solution(rx, ry, bx, by))