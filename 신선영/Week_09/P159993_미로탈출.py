from collections import deque

def solution(maps):
    def find(i, j, w, cnt): # w: 레버를 찾는지 출구를 찾는지 여부, cnt: 현재까지 소요시간
        visited = [[0] * c for _ in range(r)]
        visited[i][j] = 1

        q = deque()
        q.append([i, j, cnt])
        while q:
            ii, jj, cntt = q.popleft()
            for k in range(4):
                ni, nj = ii + di[k], jj + dj[k]

                if 0 <= ni < r and 0 <= nj < c and maps[ni][nj] == w:
                    if w == "L":
                        # 레버를 찾으면 좌표와 현재까지 소요 시간 리턴
                        return [ni, nj, cntt + 1]
                    else:
                        # 출구를 찾으면 소요 시간만 출력
                        return cntt

                if 0 <= ni < r and 0 <= nj < c and visited[ni][nj] == 0 and maps[ni][nj] != "X":
                    visited[ni][nj] = 1
                    q.append([ni, nj, cntt + 1])
        
        # 출구 찾지 못한 경우 -1
        if w == "E":
            return -1
        
    
    c = len(maps[0])
    r = len(maps)
    answer = 0
    
    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    
    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'S':
                lever = find(i, j, "L", 1)
                # 레버 찾지 못한 경우 -1
                if lever == None:
                    return -1
                else:
                    return find(lever[0], lever[1], "E", lever[2])
