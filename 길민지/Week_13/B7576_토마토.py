dx = [1,-1,0,0]
dy = [0,0,1,-1]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)] 


def solution():
  # 익은 토마토 체크
  queue = []
  cnt = 0
  for i in range(N):
    for j in range(M):
      if box[i][j] == 1: 
        queue.append([i, j, 0])
      elif box[i][j] == 0:
        cnt += 1
  # BFS
  day = 0
  while(len(queue) != 0):
    now = queue.pop(0)
    day = now[2]
    for i in range(4):
      next = [now[0]+dx[i], now[1]+dy[i], now[2]+1]
      if(next[0]<0 or next[1]<0 or next[0]>=N or next[1]>=M or box[next[0]][next[1]] != 0): 
        continue
      box[next[0]][next[1]] = 1
      cnt -= 1
      queue.append(next)
      
  # 다 익었는지 확인
  if cnt != 0:
      return -1
  return day

print(solution())