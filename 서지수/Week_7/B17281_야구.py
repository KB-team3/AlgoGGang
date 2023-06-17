import sys
from collections import deque

input=sys.stdin.readline

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# print(N)
# print(A)