def solution(n, edge):
    INF = float('inf')
    graph = [[] for _ in range(n+1)]
    cost = [INF] * (n+1)
    que = []
    
    # 인접 버텍스 정보 저장
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    que.append(1)
    cost[1] = 0
    
    while que:
        now = que.pop(0)
        for i in graph[now]:
            # 비용 갱신
            if cost[i] == INF:
                cost[i] = cost[now]+1
                que.append(i)
    
    # INF 제외한 최대값 개수 세기
    cost.remove(INF)
    max_cost = max(cost)   
    return cost.count(max_cost)