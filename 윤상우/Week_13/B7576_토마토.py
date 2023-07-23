import sys
from collections import deque
input = sys.stdin.readline
 
def bfs():
    while queue:
        x, y = queue.popleft()
        print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
 
            if 0 <= nx < n and 0 <= ny < m:
                if not graph[nx][ny]:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
    return graph
 
queue = deque()
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
 
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))    
 
result = bfs()    
print(result)
if True in map(lambda x: 0 in x, result):    
    print(-1)
else:    
    print(max(map(max, result))-1)