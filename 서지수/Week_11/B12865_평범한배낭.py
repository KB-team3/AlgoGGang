import sys

input=sys.stdin.readline

N, K=map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

arr.sort()
# print(N, K, arr)

dp=[[arr[0][0], arr[0][1]]]
# print(dp)
result=[]

# for i in range(1,N):
#     print(i)
#     print(dp[i-1][0],arr[i][0])
#     dp.append([dp[i-1][0]+arr[i][0], dp[i-1][1]+arr[i][1]])

for i in range(1,N):
    if dp[i-1][0]+arr[i][0]<=K:
        dp.append([dp[i-1][0]+arr[i][0], dp[i-1][1]+arr[i][1]])
    else:
        if arr[i][0]<=K:
            result.append(arr[i][1])
        
result.append(dp[-1][1])

print(max(result))