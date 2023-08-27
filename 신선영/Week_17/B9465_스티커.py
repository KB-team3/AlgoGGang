import sys
input = sys.stdin.readline


T = int(input())  # 테스트 케이스의 수

for tc in range(T):
    n = int(input())  # 2행 n열
  
    stickers = [list(map(int, input().split())) for _ in range(2)]
    DP = [[0] * n for _ in range(2)]

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    elif n == 2:
        print(max(stickers[0][1] + stickers[1][0], stickers[0][0] + stickers[1][1]))
    else:
        DP[0][0] = stickers[0][0]
        DP[1][0] = stickers[1][0]
        DP[0][1] = max(stickers[0][0], stickers[1][0] + stickers[0][1])
        DP[1][1] = max(stickers[1][0], stickers[0][0] + stickers[1][1])

        
        for j in range(2, n):
            for i in range(2):
                if i == 0:  # 0행의 경우
                    DP[i][j] = max(DP[i + 1][j - 2] + stickers[i][j],DP[i][j - 2] + stickers[i][j], DP[i + 1][j - 1] + stickers[i][j])
                else:  # 1행의 경우
                    DP[i][j] = max(DP[i - 1][j - 2] + stickers[i][j], DP[i][j - 2] + stickers[i][j], DP[i - 1][j - 1] + stickers[i][j])

        print(max(DP[0][n - 1], DP[1][n - 1]))
        # print(DP)
