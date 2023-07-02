import sys

input=sys.stdin.readline

N=int(input())
M=int(input())
arr=(list(map(int, input().split())))
# print(N, M, arr)
# 정렬
arr.sort()

# 거리간 차 구하기
direction=[]
for i in range(1,N):
    direction.append(arr[i]-arr[i-1])

direction.sort()
for j in range(M-1):
    direction.pop()

# print(direction)
result=0
for i in range(len(direction)):
    result+=direction[i]

print(result)