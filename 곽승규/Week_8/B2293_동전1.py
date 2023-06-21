import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 입력받기
N, K = map(int, input().split())
ary = []
for i in range(N):
    ary.append(int(input()))

DP = [0] * (K+1)
DP[0] = 1 # 0이 되기 위한 경우의 수 : 1

for coin in ary:
    for c in range(coin, K+1):
        DP[c] += DP[c - coin]

print(DP[K])
