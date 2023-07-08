from sys import stdin
input = stdin.readline

# 미로 생성
N, M = map(int, input().split())
maze = []
for _ in range(N) : 
    maze.append(list(map(int, input().split())))

# dp 점화식 설정(인덱스를 더 쉽게 다루기 위해서 각각 크기를 +1 해서 생성)
dp = [[0] * (M + 1) for _ in range (N + 1)]
for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + maze[i - 1][j - 1]

print(dp[N][M])