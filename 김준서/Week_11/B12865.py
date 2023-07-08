from collections import deque
from heapq import heappop, heappush
N, K = map(int, input().split(" "))
obj = []
for _ in range(N):
    W, V = map(int, input().split(" "))
    obj.append([W,V])
def solution(N, K):
    dp = [[0 for _ in range(N)] for _ in range(K+1)]
    for weight in range(1, K+1):
        for p in range(N):
            W, V = obj[p]
            if p==0:
                if weight<W:
                   continue
                else:
                    dp[weight][p]=V
            elif weight<W:
                dp[weight][p]=dp[weight][p-1]
            else:
                dp[weight][p]=max(dp[weight-W][p-1]+V, dp[weight][p-1])
    return dp[K][N-1]
print(solution(N, K))