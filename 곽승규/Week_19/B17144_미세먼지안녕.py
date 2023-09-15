import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C, T = map(int, input().split()) # R x C, T초

ary = []
n1, n2 = 0, 0 # 공기청정기
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

for i in range(R):
  tmp = list(map(int, input().split()))
  ary.append(tmp)

# 공기청정기
for i in range(R):
  if ary[i][0] == -1:
    n1 = i
    n2 = i+1
    break

# 미세먼지 확산하는 함수
def mise(i, j, tmp):
  if ary[i][j] not in (0, -1):
    count = 0 # 상하좌우 중 몇 개로 퍼졌는지 체크
    for k in range(4):
      nx, ny = i + dx[k], j + dy[k]
      if (nx < 0 or nx >= R) or (ny < 0 or ny >= C):
        continue
      elif ary[nx][ny] != -1:
        tmp[nx][ny] += ary[i][j] // 5
        count += 1
      else:
        continue
    tmp[i][j] -= (ary[i][j] // 5) * count

def airClean(n1, n2):
  i, j = n1, 0 # 공기청정기 좌표
  temp = 0
  # 반시계방향
  while 0 <= j + 1 < C:
    temp, ary[i][j + 1] = ary[i][j + 1], temp
    j += 1
  while 0 <= i - 1 < R:
    temp, ary[i - 1][j] = ary[i - 1][j], temp
    i -= 1
  while 0 <= j - 1 < C:
    temp, ary[i][j - 1] = ary[i][j - 1], temp
    j -= 1
  while 0 <= i + 1 < R and ary[i + 1][j] != -1:
    temp, ary[i + 1][j] = ary[i + 1][j], temp
    i += 1
    
  # 시계방향
  i, j = n2, 0 # 공기청정기 좌표
  temp = 0
  while 0 <= j + 1 < C:
    temp, ary[i][j + 1] = ary[i][j + 1], temp
    j += 1
  while 0 <= i + 1 < R:
    temp, ary[i + 1][j] = ary[i + 1][j], temp
    i += 1
  while 0 <= j - 1 < C:
    temp, ary[i][j - 1] = ary[i][j - 1], temp
    j -= 1
  while 0 <= i - 1 < R and ary[i - 1][j] != -1:
    temp, ary[i - 1][j] = ary[i - 1][j], temp
    i -= 1
    
# t초간 실행
for t in range(T):
  # 미세먼지 확산하기
  tmp = [[0]*C for _ in range(R)] # 변화된 걸 저장하는 함수
  for i in range(R):
    for j in range(C):
      mise(i,j, tmp)
      
  for i in range(R):
    for j in range(C):
      ary[i][j] += tmp[i][j]

  # 공기청정기 돌리기
  airClean(n1, n2)

answer = 0
for i in range(R):
  answer += sum(ary[i])

print(answer + 2)