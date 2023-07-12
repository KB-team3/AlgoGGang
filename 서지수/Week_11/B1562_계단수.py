import sys

input=sys.stdin.readline

N=int(input())

dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N+1)]
for k in range(1, 10):
    dp[1][k][1 << k] = 1

for length in range(N):
    for last in range(10):
        for bit in range(1024):
            if last < 9:
                next_bit = bit | (1 << (last + 1))
                dp[(length + 1)][last + 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last + 1][next_bit] %= 1000000000

            if last > 0:
                next_bit = bit | (1 << (last - 1))
                dp[(length + 1)][last - 1][next_bit] += dp[length][last][bit]
                dp[(length + 1)][last - 1][next_bit] %= 1000000000

answer = 0
for last in range(10):
    answer += dp[N][last][1023]
    answer %= 1000000000

print(answer)