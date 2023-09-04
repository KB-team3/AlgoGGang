def solution():
  # 입력
  n = int(input())
  sticker = [list(map(int, input().split())) for _ in range(2)]

  dp = [[0]*n for _ in range(3)]
  dp[0][0] = sticker[0][0]
  dp[1][0] = sticker[1][0]

  for i in range(1, n):
    # 위에꺼 선택
    dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + sticker[0][i]
    # 아래꺼 선택
    dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + sticker[1][i]
    # 둘 다 선택 X
    dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

  print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))
T = int(input())

for _ in range(T):
  solution()
