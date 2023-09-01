from collections import deque


# i : 아직 방문하지 않은 섬의 좌표, maps : 지도, visit : 방문여부
def bfs(i, maps, visit) : 

    # 첫 방문 위치의 식량
    cnt = int(maps[i[0]][i[1]])     # 문자열 int값으로 변환
    visit[i[0]][i[1]] = 1
    q = deque()
    q.append(i)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q : 
        x, y = q.popleft()
        for i in range(4) : 
            nx = x + dx[i]
            ny = y + dy[i]

            # maps의 범위 넘어서면 정지
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]) : 
                continue
            
            # 바다 만나면 정지
            if maps[nx][ny] == "X" : 
                continue

            if visit[nx][ny] == 0 : 
                visit[nx][ny] = 1
                cnt += int(maps[nx][ny])
                q.append((nx, ny))
    return cnt


def solution(maps) : 
    answer = []
    island = []     # 섬 좌표(바다가 아닌 부분)
    visit = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)) : 
        for j in range(len(maps[0])) : 
            # 바다가 아닌 좌표 append
            if maps[i][j] != "X" : 
                island.append((i, j))

    # 섬이 하나도 없을 경우
    if len(island) == 0 : 
        return[-1]
    
    for i in island : 
        if visit[i[0]][i[1]] == 0 : 
            answer.append(bfs(i, maps, visit))

    return sorted(answer)
