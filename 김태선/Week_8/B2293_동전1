from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
coins = []

for i in range(n) :
    coins.append(int(input()))

# i원이 되는 경우의 수
dp = [0]  * (k + 1)
dp[0] = 1
# dp[i] => i원을 만들 때 가능한 경우의 수
# dp[0] => 동전 하나를 사용하는 경우

for c in coins :
    for i in range(c, k + 1) : # i원
        dp[i] += dp[i - c]
# c원 동전으로 i원 만들기 => i - c원을 만들 후 c원을 추가
# 즉, c원으로 동전을 만드는 경우의 수 => dp[i - c]원


print(dp[k])