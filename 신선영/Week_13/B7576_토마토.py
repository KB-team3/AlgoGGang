from collections import deque
def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            ni, nj = x + di[i], y + dj[i]
            if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] == 0:
                tomatoes[ni][nj] = tomatoes[x][y] + 1
                q.append([ni, nj])


M, N = map(int, input().split())    # M: 가로, N: 세로
tomatoes = [list(map(int, input().split())) for _ in range(N)]
q = deque()

start = [0, 0]
for i in range(N):      # 시작점 구하기
    for j in range(M):
        if tomatoes[i][j] == 1:
            start = [i, j]
            q.append(start)


# 오른쪽, 아래, 왼쪽, 위
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

bfs()

# 2차원 리스트 전체 최대
ans = max(map(max, tomatoes)) - 1  # 1이 익은토마토니까 1부터 시작 - 빼줌

# 다 익지 못한 경우 예외처리 
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            ans = -1

print(ans)
