# 다익스트라 알고리즘 (BFS)
import sys
from collections import deque

def solution(n, edge):
    answer = 0
    distance = [-1] * (n+1)
    visited = [False] * (n+1)
    
    ary = [[] for _ in range(n+1)] # 인접리스트 생성
    for ed in edge:
        s, e = ed[0], ed[1]
        ary[s].append(e)
        ary[e].append(s)
    
    distance[1] = 0
    queue = deque()
    queue.append(1)
    visited[1] = True
    
    while queue:
        now = queue.popleft()
        for a in ary[now]:
            if not visited[a]:
                distance[a] = distance[now] + 1
                queue.append(a)
                visited[a] = True
    maxValue = max(distance)
    
    answer = distance.count(maxValue)
    return answer