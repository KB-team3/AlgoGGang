N, M = map(int, input().split(" "))
board = []
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
for _ in range(N):
    board.append(list(map(int,input().split(" "))))
sumx = board[0][0]
sumy = board[0][0]
dp[0][0]=board[0][0]
for i in range(1,N):
    sumx+=board[i][0]
    dp[i][0]+=sumx
for i in range(1,M):
    sumy+=board[0][i]
    dp[0][i]+=sumy
for i in range(1,N):
    for j in range(1,M):
        dp[i][j]=max(dp[i-1][j],dp[i][j-1])+board[i][j]
print(dp[N-1][M-1])