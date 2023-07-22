from collections import deque
from sys import stdin
input = stdin.readline

# 상하좌우 설정
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

m, n = map(int, input().split(" "))

# 그래프 생성
graph = []
for i in range(n) :
    graph.append(list(map(int, input().split(" "))))

# 큐 생성
q = deque()

for i in range(n) : 
    for j in range(m) :
        if graph[i][j] == 1 : 
            q.append((i, j))

# bfs
while q :
    x, y = q.popleft()

    for i in range(4) : 
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m : 
            continue

        if graph[nx][ny] == 0 : 
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

# 결과값 출력 (??? 이 부분 이해안감)
result = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit()
    result = max(result, max(graph[i]))

print(result - 1)


