import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 입력받기
N = int(input())
ary = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  ary.append(tmp)
  
# 상, 좌, 하, 우
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

sharkSize = 2 # 처음은 크기 2임.
cnt = 0 # 상어가 먹는거
answer = 0

# 우선,, 아기 상어의 위치 파악하기
sharkX, sharkY = 0,0
for i in range(N):
  for j in range(N):
    if ary[i][j] == 9:
      ary[i][j] = 0
      sharkX = i
      sharkY = j
      break

def bfs(x, y):
  global sharkSize
  # 방문체크
  queue = deque()
  queue.append((x,y))
  
  visited = [[0 for _ in range(N)] for _ in range(N)]
  distance = [[0 for _ in range(N)] for _ in range(N)]
  can_eat_fish = []
  
  while queue:
    now = queue.popleft()
    for k in range(4):
      nx, ny = now[0] + dx[k], now[1] + dy[k]
      
      if 0 <= nx < N and 0 <= ny < N: # 범위 안에 있다면!
        if ary[nx][ny] <= sharkSize and visited[nx][ny] != 1: # 상어몸집보다 작고 방문하지 않았다면 이동가능
          visited[nx][ny] = 1
          queue.append((nx,ny))
          distance[nx][ny] = distance[now[0]][now[1]] + 1
          
          if ary[nx][ny] < sharkSize and ary[nx][ny] != 0: # 상어몸집보다 작다면 먹을 수 있음 (0제외)!
            can_eat_fish.append([nx, ny, distance[nx][ny]])
   
  can_eat_fish.sort(key = lambda x : (x[2], x[0], x[1])) # 거리, x, y 순으로 정렬 (왜냐면 위에꺼가 우선순위이므로)
  return can_eat_fish

while True:
  fish = bfs(sharkX, sharkY)
  
  print(fish)
  if len(fish) == 0: # 물고기가 없다면
    print(answer)
    exit(0)
  
  sharkX, sharkY, m = fish[0]
  
  cnt += 1 # 물고기 한마리 먹음
  
  if sharkSize == cnt:
    cnt = 0 # 초기화
    sharkSize += 1 # 몸집 키우기 
  
  ary[sharkX][sharkY] = 0 #먹은 자리는 0으로 바꿈
  answer += m  # 이동한거리 더하기    
