# 입력
N, K = map(int, input().split())

if K==1:
  print(1)
  exit(0)

# dp[n][k] = k개의 숫자로 n을 만들 수 있는 개수
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 초기조건
for k in range(1, K+1):
  dp[0][k] = 1
for n in range(N+1):
  dp[n][1] = 1

# 점화식
for i in range(1, N+1):
  for j in range(2, K+1):
      dp[i][j] = dp[i-1][j]+dp[i][j-1]

# 출력
print(dp[N][K]%1000000000)