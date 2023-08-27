from sys import stdin
input = stdin.readline

t = int(input())

for _ in range(t) : 
    n = int(input())
    # dp배열 초기화
    dp = [list(map(int, input().split())) for _ in range(2)]

    # 열 2개 이상부터 dp 동작 가능
    if n >= 2 : 
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    
    # dp 점화식 생성
    for i in range(2, n) : 
        dp[0][i] += max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] += max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))
    