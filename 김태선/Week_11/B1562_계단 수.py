from sys import stdin
input = stdin.readline

mod = 1000000000
M = (1 << 10) - 1
n = int(input())

dp = [[0] * (M + 1) for _ in range(10)]
for i in range(1, 10) : 
    dp[i][1 << i] = 1
for _ in range(2, n + 1) : 
    next_dp = [[0] * (M + 1) for _ in range(10)]
    for i in range(10) : 
        for j in range(M + 1) :
            if i > 0 : 
                next_dp[i][j | (1 << i)] = (
                    next_dp[i][j | (1 << i)] + dp[i - 1][j]) % mod
            if i < 9 : 
                next_dp[i][j | (1 << i)] = (
                    next_dp[i][j | (1 << i)] + dp[i + 1][j]) % mod
    dp = next_dp

answer = sum(dp[i][M] for i in range(10)) % mod
print(answer)