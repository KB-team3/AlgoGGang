import sys
input = sys.stdin.readline
from collections import deque


def BFS(i, j):
    cases = []
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1
    q = deque()
    q.append([0, i, j])
    di = [0, -1, 0, 1]
    dj = [-1, 0, 1, 0]

    while q:
        cnt, ii, jj= q.popleft()
        for k in range(4):
            ni, nj = ii + di[k], jj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0:
                # 먹을 수 있는 경우
                if space[ni][nj] < size and space[ni][nj] != 0:
                    cases.append([cnt + 1, ni, nj])

                # 지나갈 수만 있는 경우
                if space[ni][nj] <= size:
                    v[ni][nj] = 1
                    q.append([cnt + 1, ni, nj])
  
    return sorted(cases)

ans = 0
size = 2

N = int(input())
space = [[*map(int, input().split())] for _ in range(N)]

# 시작 시 상어의 위치 찾기 
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            si, sj = i, j

cnts = 0
while 1:

    space[si][sj] = 0
    cases = BFS(si, sj)
    if not cases:
        break
    cnt, si, sj = cases[0]
    ans += cnt
    cnts += 1

    if cnts == size:
        size += 1
        cnts = 0

print(ans)
