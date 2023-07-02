import sys

input=sys.stdin.readline

N, M=map(int, input().split())
arr = []
for i in range(M):
    arr.append(input()[:-1])

print(N, M, arr)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
cnt=0

def gogo(start, end):
    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        for i in range(4):
            x=start+dx[i]
            y=start+dy[i]
            cnt+=1


for i in range(N):
    for j in range(M):
        if arr[i][j]=="R":
            gogo(i, j)

print(cnt)