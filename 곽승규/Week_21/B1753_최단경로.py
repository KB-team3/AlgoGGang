# 최단경로
# 다익스트라 활용하기

import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split()) # 정점개수, 간선개수
K = int(input()) # 시작 정점 번호
distance = [sys.maxsize] * (V+1) # 거리저장리스트, 충분히 큰 수로 초기화
visited = [False] * (V+1) # 방문리스트
myList = [[] for _ in range(V+1)] # 인접리스트
q = PriorityQueue()

for _ in range(E):
  u, v, w = map(int, input().split())
  myList[u].append((v,w))

q.put((0,K)) # 0: 가중치, K: 시작점
distance[K] = 0 # 시작점의 거리는 0임

while q.qsize() > 0:
  current = q.get()
  current_value = current[1]
  if visited[current_value]:
    continue
  visited[current_value] = True
  for tmp in myList[current_value]:
    next = tmp[0] # 다음 노드
    value = tmp[1] # 가중치
    if distance[next] > distance[current_value] + value: # 최소 거리로 업데이트
      distance[next] = distance[current_value] + value
      q.put((distance[next], next))

for i in range(1, V+1):
  if visited[i]:
    print(distance[i])
  else:
    print('INF')