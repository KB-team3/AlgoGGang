def dfs(start, check, n, computers):
    check[start] = 1
    for nn in range(n):
        if computers[start][nn] == 1 and check[nn] == 0:
            dfs(nn, check, n, computers)

def solution(n, computers):
    answer = 0
    check = [0 for _ in range(n)]
    
    for i in range(n):
        if check[i] == 1: 
            continue
        answer += 1
        dfs(i, check, n, computers)
    return answer