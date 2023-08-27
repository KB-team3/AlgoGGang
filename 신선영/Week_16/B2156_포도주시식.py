import sys
input = sys.stdin.readline

N = int(input())  # 포도주 잔의 개수
L = []

for _ in range(N):
    L.append(int(input()))

DP = [0] * N

DP[0] = L[0]
if N > 1: DP[1] = L[0] + L[1]
if N > 2: DP[2] = max(L[2] + L[1], L[2] + L[0], DP[1])


for i in range(3, N):
    DP[i] = max(DP[i - 1], DP[i - 3] + L[i - 1] + L[i], DP[i - 2] + L[i])

print(DP[N - 1])





