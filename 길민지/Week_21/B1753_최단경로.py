import heapq
import sys

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]

cost = [INF] * (V+1)
que = []

for i in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append([v,w])

def func(start):
  cost[start] = 0
  heapq.heappush(que, [0, start])

  while que:
    now_w, now_node = heapq.heappop(que)
    if cost[now_node] < now_w:
      continue
    for next_node, weight in graph[now_node]:
      next_w = now_w + weight

      if next_w < cost[next_node]:
        cost[next_node] = next_w
        heapq.heappush(que, [next_w, next_node])

func(K)

for i in cost[1:]:
  print(i if i != INF else "INF")
