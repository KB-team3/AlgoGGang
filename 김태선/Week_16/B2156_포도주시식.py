from sys import stdin
input = stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]   # dp와 인덱스 맞추기

dp = [0] * (n + 1)
dp[1] = wine[1]
# n 범위가 1 이상이므로 에외 분기 삽입
if n > 1 : 
    dp[2] = wine[1] + wine[2]

for i in range(3, n + 1) : 
    # 점화식
    dp[i] = max(dp[i - 2] + wine[i], dp[i - 1], dp[i - 3] + wine[i - 1] + wine[i])
    ''' 
    1. dp[i - 2] + wine[i] : 첫번째, 세번째 꺼 먹었을 때
    2. dp[i - 1] : 첫번째, 두번째 꺼 먹었을 때
    3. dp[i - 3] + wine[i - 1] + wine[i] : 두번째, 세번째 꺼 먹었을 때
    '''

print(dp[n])