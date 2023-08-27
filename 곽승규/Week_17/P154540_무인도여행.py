from collections import deque

def solution(maps):
    answer = []
    ary = maps
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    def bfs(x, y):
        sum = int(ary[x][y])
        queue = deque([(x,y)])
        visited[x][y] = True
             
        # 상하좌우
        dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
        
        while queue:
            cx, cy = queue.popleft()
            
            # 상하좌우 탐색
            for i in range(4):
                nx, ny = dx[i] + cx, dy[i] + cy
                if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and ary[nx][ny] != 'X' and not visited[nx][ny]:
                    sum += int(ary[nx][ny])
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        return sum
            
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if ary[i][j] == 'X' or visited[i][j]:
                continue
            answer.append(bfs(i, j))
    
    return [-1] if len(answer) == 0 else sorted(answer)