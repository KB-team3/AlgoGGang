import copy

global rotate
global direction
global max_count

# 1. cctv가 감시하는 방향 이동하며 체크
def move(map, i, j, dir, count):
  # cctv 막히면 종료
  if i<0 or j<0 or i>=N or j>=M or map[i][j] == 6:
    return count
    
  # 빈칸일 경우 count 증가 후 방문 체크
  if map[i][j] == 0:
    count+=1
    map[i][j] = -1
    
  # 다음 칸으로 이동
  if dir%2 == 0:
    count=move(map, i+dir-1, j, dir, count)
  else:
    count=move(map, i, j+2-dir, dir, count)
  return count

# 2. cctv 감시 영역 세기
def check(map, cctv):
  count = 0
  for c in cctv: # cctv 결정
    for d in direction[c[2]]: # 방향 
      count+=move(map, c[0], c[1], (d+c[3])%4, 0)
  return count

# 3. 각 cctv 회전 결정
def rotation(i, cctv, map):
  global max_count
  if i == len(cctv):
    checkmap = copy.deepcopy(map)
    count = check(checkmap, cctv)
    max_count = max(count, max_count)
    return
  for j in rotate[cctv[i][2]]:
    cctv[i][3] = j
    rotation(i+1, cctv, map)

#######################################################
# 입력
N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
rotate = [[],[0,1,2,3],[0,1],[0,1,2,3],[0,1,2,3],[0]] # 회전 방향 종류
direction = [[], [0], [0,2], [0,1], [0,1,2], [0,1,2,3]] # cctv 종류별 감시 방향
none = 0 # 벽과 cctv 개수
max_count = 0 # 최대 감시 영역

# cctv 기록
cctv = []
for i in range(N):
  for j in range(M):
    if map[i][j] == 6 :
      none += 1
    if map[i][j] != 0 and map[i][j] != 6:
      none += 1
      cctv.append([i, j, map[i][j], 0]) # i, j, 카메라 종류, 방향

# 감시영역 탐색
rotation(0, cctv, map)

# 출력
print(N*M-none-max_count)
