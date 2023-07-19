import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

M, N = map(int, input().split()) # M, N 입력받기

# 토마토 값 입력받기
ary = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    ary.append(tmp)

# 방향 리스트
dx = [0, 0, -1, 1] # 아래, 위, 왼, 오
dy = [1, -1, 0, 0]

count = 0
queue = deque() # 큐생성

# 익은 토마토 위치를 큐에 넣기
for i in range(N):
    for j in range(M):
        if ary[i][j] == 1:
            queue.append((i, j, 0))

while queue:
    x, y, day = queue.popleft()
    count = day
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and ary[nx][ny] == 0:
            ary[nx][ny] = 1
            queue.append((nx, ny, count + 1))


for i in range(N):
    if 0 in ary[i]:
        print("-1")
        sys.exit()
  
print(count)