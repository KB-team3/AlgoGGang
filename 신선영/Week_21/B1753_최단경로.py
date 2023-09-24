import sys
input = sys.stdin.readline


V, E = map(int, input().split())  # V: 정점의 개수, E: 간선의 개수
K = int(input())  # 시작 정점의 번호

graph = [[] for _ in range(V + 1)]  # 정점: 1부터 시작

visited = [0] * (V + 1)
distance = [1e9] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance[K] = 0
visited[K] = 1

for g in graph[K]:
    distance[g[0]] = g[1]

for i in range(V - 1):
    min_v = 1e9
    idx = 0
    for j in range(1, V + 1):
        if distance[j] < min_v and not visited[j]:
            min_v = distance[j]
            idx = j

    visited[idx] = 1

    for j in graph[idx]:
        if distance[idx] + j[1] < distance[j[0]]:
            distance[j[0]] = distance[idx] + j[1]


for i in range(1, V + 1):
    d = distance[i]
    if d == 1e9:
        print("INF")
    else:
        print(d)
