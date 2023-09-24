
answer = 0
check = []

def dfs(k, dungeons, cnt):
    global answer
    
    if answer < cnt:
        answer = cnt
    
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k and check[i] == 0:
            check[i] = 1
            dfs(k-dungeons[i][1], dungeons, cnt+1)
            check[i] = 0
        
    return 0

def solution(k, dungeons):
    global check 
    check= [0] * len(dungeons)
    
    dfs(k, dungeons, 0)
    
    return answer