# 1. permutaion 8! -> posible
# from itertools import permutations
# def solution(k, dungeons):
#     answer = -1
    
#     for p in permutations(dungeons, len(dungeons)):
#         tmp = k
#         count = 0
        
#         for need, spend in p:
#             if tmp >= need:
#                 tmp -= spend
#                 count += 1
#             else:
#                 break
#         answer = max(answer, count)    
#     return answer

# 2. dfs (backtracking)
answer = 0
def dfs(k, count, dungeons, visited):
    global answer
    if count > answer:
        answer = count
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], count+1, dungeons, visited)
            visited[i] = False
    
def solution(k, dungeons):
    global answer
    
    visited = [False] * len(dungeons)
    dfs(k,0, dungeons, visited)
    return answer