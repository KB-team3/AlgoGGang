from collections import deque


def bfs(start, end, maps):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    row = len(maps)      
    cols = len(maps[0])    # 가로
    visited = [[False]*cols for _ in range(row)]
    que = deque()
    flag = False
    
    for i in range(row):
        for j in range(cols):
            if maps[i][j] == start:      
                que.append((i, j, 0))    
                visited[i][j] = True
                flag = True
                break 
        if flag: 
            break
                
    while que:
        y, x, cost = que.popleft()
        if maps[y][x] == end:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<= ny <row and 0<= nx <cols and maps[ny][nx] !='X':
                if not visited[ny][nx]:	
                    que.append((ny, nx, cost+1))
                    visited[ny][nx] = True
                    
    return -1	
        
            
def solution(maps):
    path1 = bfs('S', 'L', maps)	
    path2 = bfs('L', 'E', maps) 
    
    if path1 != -1 and path2 != -1:
        return path1 + path2
        
    return -1