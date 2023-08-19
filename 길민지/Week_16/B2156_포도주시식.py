# 입력
n = int(input())
list =  [int(input()) for _ in range(n)]

if(n==1) :
  print(list[0])
  exit()
elif(n==2):
  print(list[0]+list[1])
  exit()
  
# DP
dp = [0]*n
dp[0] = list[0]
dp[1] = list[0] + list[1]
dp[2] = max(dp[0]+list[2], list[1]+list[2], dp[1])
for i in range(3, n):
  # 마시기
  drink = max(dp[i-2] + list[i], dp[i-3] + list[i-1] + list[i])
  # 안 마시기
  nodrink = dp[i-1]
  dp[i] = max(drink, nodrink)

print(dp[n-1])