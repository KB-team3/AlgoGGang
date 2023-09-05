def solution(maps):
    def dfs(i, j, cnt):
        global answer
        if len(answer) > 0 and cnt > min(answer):
            return
        
        if i == (n - 1) and j == (m - 1):
            answer.append(cnt)
            return
    
        
        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]
        
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < n and 0 <= nj < m and maps[ni][nj] == 1 and v[ni][nj] == 0:
                v[ni][nj] = 1
                dfs(ni, nj, cnt + 1)
                v[ni][nj] = 0
                
        
    n = len(maps)
    m = len(maps[0])
    
    v = [[0] * m for _ in range(n)]
    
    global answer
    answer = []
    dfs(0, 0, 1)
    
    return min(answer) if len(answer) > 0 else -1
