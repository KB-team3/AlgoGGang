import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())  # 물건 개수, 최대 무게

DP = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# 값 입력받기
arr = [(0, 0)]
for _ in range(N):
    W, V = map(int, input().split())
    arr.append((W, V))

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = arr[i][0]
        v = arr[i][1]

        if j < w:  # 현재의 weight보다 작으면
            DP[i][j] = DP[i - 1][j]  # 이전 값 그대로 가지고 옴
        else:
            DP[i][j] = max(v + DP[i - 1][j - w], DP[i - 1][j])

print(DP[N][K])
