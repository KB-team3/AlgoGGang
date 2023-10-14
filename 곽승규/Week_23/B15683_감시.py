import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# N, M 받기
N, M = map(int, input().split())
ary = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  ary.append(tmp)

# 남, 동, 북, 서
dx, dy = [1,0,-1,0], [0,1,0,-1]

d = {
  1 : [[0],[1],[2],[3]],
  2 : [[0,2], [1,3]],
  3 : [[0,1], [1,2], [2,3], [3,0]],
  4 : [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],
  5 : [[0,1,2,3]]
}
def move(x, y, direction, space_copy):
  for di in direction:
    nx, ny = x, y
    
    while True:
      nx = nx + dx[di]
      ny = ny + dy[di]
      
      if (nx < 0 or nx >= N or ny < 0 or ny >= M) or space_copy[nx][ny]==6:
        break
      # 빈칸이 아니면
      if space_copy[nx][ny] != 0:
        continue
      space_copy[nx][ny] = '#'

# 사각지대 구하는 함수
def zero_cnt(space_copy):
  global answer
  cnt = 0
  for i in space_copy:
    cnt += i.count(0)
  
  answer = min(answer, cnt)


def dfs(level, space):
  space_copy = [[j for j in space[i]] for i in range(N)]
  
  if level == len(cctv):
    zero_cnt(space_copy)
    return
  
  number, x, y = cctv[level]
  
  # number번째 cctv에 대해 가능한 모든 방향을 순차적으로 고려 
  for di in d[number]:    
    move(x, y, di, space_copy)
    dfs(level+1, space_copy)   # level+1번째 cctv를 고려
    space_copy = [[j for j in space[i]] for i in range(N)]

# cctv 위치 확인
cctv = deque()
answer = 0
for i in range(N):
  for j in range(M):
    if ary[i][j] != 6 and ary[i][j] != 0:
      cctv.append((ary[i][j], i, j)) # cctv번호, 좌표
    if ary[i][j] == 0:
      answer += 1

dfs(0, ary)
print(answer)