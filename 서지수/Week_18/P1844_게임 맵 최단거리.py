from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
    
def solution(maps):
    N = len(maps[0]) # 행 크기
    M = len(maps) # 열 크기
    visited = [[0 for _ in range(N)] for _ in range(M)]
    visited[0][0] = 1
    
    queue = deque()
    queue.append((0, 0))
    while len(queue) :
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx>= M or ny < 0 or ny >= N :
                continue
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        
    if visited[M-1][N-1] == 0 :
        return -1
    return visited[M-1][N-1]