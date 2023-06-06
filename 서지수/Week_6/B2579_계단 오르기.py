import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

steps = []
for i in range(N):
    steps.append(int(input()))

# print(N)
# print(steps)

dp=[]
dp.append(steps[0])
dp.append(max(steps[0]+steps[1],steps[1])) 
dp.append(max(steps[0]+steps[2],steps[1]+steps[2])) 
for i in range(3,N):
    dp.append(max(dp[i-2] + steps[i] , dp[i-3] + steps[i] + steps[i - 1]))

print(dp.pop())