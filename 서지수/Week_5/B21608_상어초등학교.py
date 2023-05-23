import sys
from collections import deque
input=sys.stdin.readline

N = int(input())
A = []
for i in range(N*N):
    A.append(list(map(int, input().split())))

graph = [[-1]*(N) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N*N):



# 만족도
def satisfy():
    