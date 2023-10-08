import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
sX, sY, direction = map(int, input().split())
ary = []
for i in range(N):
  tmp = list(map(int, input().split()))
  ary.append(tmp)

visited = [[0] * M for _ in range(N)]

# 북, 동, 남, 서
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
visited[sX][sY] = 1 # 로봇청소기가 있는 칸은 빈칸이므로!
count = 1 # 첫번째 청소기 위치는 청소함.

while True:
  flag = 0
  for _ in range(4):
    direction = (direction + 3) % 4 # 왼쪽으로 돌림
    nx, ny = sX + dx[direction], sY + dy[direction]
    
    if 0 <= nx < N and 0 <= ny < M and ary[nx][ny] == 0:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1 # 청소함.
        count += 1
        sX = nx
        sY = ny
        flag = 1
        break
      
  # 네 방향 모두 청소 할 수 없으면
  if flag == 0:
    if ary[sX-dx[direction]][sY-dy[direction]] == 1: # 현재 바라보는 방향에서 후진함.
      print(count)
      break
    else:
      sX, sY = sX-dx[direction], sY-dy[direction]
    