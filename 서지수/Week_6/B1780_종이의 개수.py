import sys
from collections import deque

input=sys.stdin.readline

N=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]
papers = []
for i in range(N):
    papers.append(list(map(int, input().split())))

# print(N)
# print(papers)

minus=0
zero=0
plus=0

def divide(row, col, n):
    global minus, zero, plus
    check=papers[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if papers[i][j]!=check:#처음 값이랑 값이 다름=다른 넘버
                for a in range(3):
                    for b in range(3): #어차피 다 3의 제곱수니까 다 3 단위로
                        divide(row+a*n//3, col+b*n//3, n//3) #원래의 시작점+@
                return
            
    if check==-1:
        minus+=1
    elif check==0:
        zero+=1
    elif check==1:
        plus+=1


divide(0,0,N)
print(minus)
print(zero)
print(plus)