# [BOJ] 16948. 데스 나이트  2023-04-27

import sys
input = sys.stdin.readline
from collections import deque # 왼쪽에서 넣기 위해 deque 사용


def bfs(i, j):  # 최소값: bfs 사용
  global ans
  Q = deque()
  visited[i][j] = 1
  Q.append([i, j, 0])   # 초기값 넣고 시작, c: 단계(0으로 시작)
  
  # 문제에서 정의한 탐색 범위
  di = [-2, -2, 0, 0, 2, 2]
  dj = [-1, 1, -2, 2, -1, 1]

  while Q:
      a, b, c = Q.popleft()
      
      if a == r2 and b == c2:   # 목표값 찾는 경우 현재까지의 단계를 답으로 지정
          ans = c
          return

      for k in range(6):
          ni, nj = a + di[k], b + dj[k]
          if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
              visited[ni][nj] = 1
              # 다음 단계 탐색 시 c값에 +1
              Q.append([ni, nj, c + 1])
              


N = int(input())  # 체스판의 크기: N * N
r1, c1, r2, c2 = map(int, input().split())
visited = [[0] * N for _ in range(N)]   # 방문 체크 리스트
ans = -1  # 답 찾을 수 없는 경우 답은 -1

bfs(r1, c1)
print(ans)
