import sys
from collections import deque

input=sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(len(A[i])):
        if j==0:
            A[i][j]+=A[i-1][j]
        elif j==i:
            A[i][j]+=A[i-1][j-1]
        else:
            A[i][j]+=max(A[i-1][j-1], A[i-1][j])
       
print(max(A[N-1]))
