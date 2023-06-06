import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
# 계단의 값들 입력받기
S = [int(input()) for _ in range(N)]
# print(S)

DP = [0] * 301
# print(DP[-1])

if N <= 2:
    print(sum(S))
else:
    DP[0] = S[0]
    DP[1] = S[1] + S[0]
    for i in range(2, N):
        DP[i] = max(S[i] + DP[i - 2], S[i] + S[i - 1] + DP[i - 3])
    print(DP[N - 1])
