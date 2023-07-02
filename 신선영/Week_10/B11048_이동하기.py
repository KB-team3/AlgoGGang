# [BOJ] 11048. 이동하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n가지 종류, k원

# 인덱스에러 방지 위해 미로의 왼쪽, 위를 0으로 채우고 시작
maze = [[0] * (m + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
candy = [[0] * (m + 1) for _ in range(n + 1)]

# 왼쪽, 위, 왼쪽 대각선 위를 비교하면서 현재까지 경로에서 최대값을 저장
for i in range(1, n + 1):
    for j in range(1, m + 1):
        candy[i][j] = max(candy[i - 1][j], candy[i][j - 1], candy[i - 1][j - 1]) + maze[i][j]

# 도착시 최대값 출력
print(candy[n][m])
