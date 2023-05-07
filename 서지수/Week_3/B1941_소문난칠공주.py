import sys
input=sys.stdin.readline
from collections import deque

graph = [list(input()) for _ in range(5)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# print(graph)

def bfs(x, y):
     que = deque()
     que.append((x, y))
    # graph[x][y]
    # isVisited도 구해야하나
      while que:
        x, y= que.popleft()
        for i in range(4):
            nx, ny = x+dx, y+dy
            if (0 <= nx < 5) and (0 <= ny < 5) and graph[nx][ny] == -1:
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y]+1