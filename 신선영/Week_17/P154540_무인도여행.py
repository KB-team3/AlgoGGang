from collections import deque

def solution(maps):
    def travel(i, j):
        stay = int(newmap[i][j])
        q = deque()
        q.append([i, j])
        V[i][j] = 1

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        while q:
            ii, jj = q.popleft()
            for k in range(4):
                ni, nj = ii + di[k], jj + dj[k]
                if 0 <= ni < h and 0 <= nj < w and V[ni][nj] == 0 and newmap[ni][nj] != 'X':
                    q.append([ni, nj])
                    V[ni][nj] = 1
                    stay += int(newmap[ni][nj])
                    newmap[ni][nj] = 'X'
    
        return stay
    
    answer = []
    h = len(maps)   # 세로 길이
    w = len(maps[0])    # 가로 길이
    newmap = []
    for m in maps:
        newmap.append(list(m))
    
    V = [[0] * w for _ in range(h)]
    
    for i in range(h):
        for j in range(w):
            if newmap[i][j] != 'X':
                answer.append(travel(i, j))
    
    return [-1] if len(answer) == 0 else sorted(answer)
