from sys import stdin
input = stdin.readline

# n = 물건 갯수, k = 무게 제한
n, k = map(int, input().split()) 
stuff = [[0,0]]
dp = [[0] * (k+1) for _ in range(n + 1)]

for _ in range(n) : 
    stuff.append(list(map(int, input().split())))

for i in range(1, n + 1) : 
    for j in range(1, k + 1) : 
       
       # w = 무게, v = 가치
        w, v = stuff[i]
        if j >= w : # 현재 물건 담을 수 있다. 
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
        else : # dp 무게가 현재 물건의 무게보다 작아서 물건을 담지 못한다.
            dp[i][j] = dp[i - 1][j]

print(dp[i][k])