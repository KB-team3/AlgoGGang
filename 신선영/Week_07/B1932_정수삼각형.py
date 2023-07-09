import sys
input=sys.stdin.readline

N=int(input())  # 삼각형의 크기
DP = [[] for _ in range(N)]
DP[0].append(int(input()))


for i in range(1, N):
    L = list(map(int, input().split()))
    DP[i].append(DP[i - 1][0] + L[0])
    for j in range(1, len(L) - 1):
        DP[i].append(max(DP[i - 1][j - 1] + L[j], DP[i - 1][j] + L[j]))
    DP[i].append(DP[i - 1][-1] + L[-1])

print(max(DP[-1]))
