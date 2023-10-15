global visited 

def DFS(s):
  visited[s] = True
  for i in range(N):
    if city[s][i] == 1 and visited[i] is False:
      DFS(i)
      
# 입력
N = int(input())
M = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
travel = list(map(int, input().split()))
visited = [False] * N

# 방문 체크
DFS(travel[0]-1)

# 출력
for t in travel:
  if visited[t-1] is False:
    print("NO")
    exit(0)
print("YES")
  