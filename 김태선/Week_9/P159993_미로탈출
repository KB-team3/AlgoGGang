from collections import deque

def solution(maps):
    # 배열 생성
    n, m = len(maps), len(maps[0])

    # 상하좌우 생성
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # bfs
    def search(start, goal) : 
        # 방문체크
        visited = [[0] * m for _ in range(n)]

        # 큐 생성
        q = deque([(start[0], start[1], 0)])
        visited[start[0]][start[1]] = 1

        while q : 
            a, b, cnt = q.popleft()
            
            # 목표도달 경우
            if (a, b) == goal : 
                return cnt
            
            for d in range(4) : 
                y = a + dy[d]
                x = b + dx[d]

                if 0 <= y < n and 0 <= x < m and maps[y][x] != 'X' and visited[y][x] == 0 : 
                    visited[y][x] = 1
                    q.append((y, x, cnt + 1))
        
        return 0
    

    # 좌표 설정 (시작, 레버, 탈출구)
    check = [(), (), ()]

    for i in range(n) : 
        for j in range(m) : 
            if maps[i][j] == 'S' : 
                check[0] = (i, j)
            
            elif maps[i][j] == 'L' :
                check[1] = (i, j)

            elif maps[i][j] == 'E' : 
                check[2] = (i, j)

    # 시작에서 레버까지 거리 1
    rs1 = search(check[0], check[1])

    # 레버에서 탈출구까지 거리 2
    rs2 = search(check[1], check[2])

    if rs1 != 0 and rs2 != 0 : 
        return rs1 + rs2
    else : 
        return -1 
