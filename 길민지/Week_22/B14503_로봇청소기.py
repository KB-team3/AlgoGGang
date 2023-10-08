# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

clean = [[0 for _ in range(M)] for _ in range(N)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
answer = 0

while True:
  # 1. 현재 칸이 청소되지 않은 경우, 청소
  if clean[r][c] == 0:
    clean[r][c] = 1
    answer += 1
  
  # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
  check = False
  for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]
    if arr[nr][nc] == 1 or clean[nr][nc] == 1:
      continue
    check = True
    break
  # 한 칸 후진
  if check is False:
    r += dr[(d+6)%4]
    c += dc[(d+6)%4]
    if arr[r][c] == 1:
      break
    else:
      continue
      
  # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
  while True:
    d = (d+3)%4 # 반시계 90도 회전
    nr = r+dr[d]
    nc = c+dc[d]
    if arr[nr][nc] == 0 and clean[nr][nc] == 0:
      r = nr
      c = nc
      break
      
print(answer)