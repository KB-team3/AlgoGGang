from collections import deque


def solution(maps) : 
    n = len(maps)
    m = len(maps[0])

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((0, 0))

    while q : 
        x, y = q.popleft()

        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m : 
                continue
            # 벽이거나 이미 방문한 경우
            if maps[nx][ny] > 1 or maps[nx][ny] == 0 : 
                continue
            # 제자리로 돌아간 경우
            if nx == 0 and ny == 0 : 
                continue

            q.append((nx, ny))
            maps[nx][ny] += maps[x][y]
    
    # 목적지 도달여부
    if maps[n - 1][m - 1] > 1 : 
        return maps[n - 1][m - 1]
    else :
        return -1

# maps=[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# print(solution(maps))