import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
r1,c1,r2,c2=map(int, input().split())
graph = [[-1]*(N) for _ in range(N)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(r, c):
    que = deque()
    que.append((r, c))
    graph[r][c] = 0
    while que:
        r, c = que.popleft()
        for dr, dc in d:
            nr, nc = r+dr, c+dc
            if (0 <= nr < N) and (0 <= nc < N) and graph[nr][nc] == -1:
                que.append((nr, nc))
                graph[nr][nc] = graph[r][c]+1

bfs(r1, c1)
print(graph[r2][c2])