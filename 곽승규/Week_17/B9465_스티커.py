import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    ary = []
    
    for i in range(2):
        tmp = list(map(int, input().split()))
        ary.append(tmp)
    if n == 1:
        print(max(ary[0][0], ary[1][0]))
        continue
    
    ary[0][1] += ary[1][0]
    ary[1][1] += ary[0][0]
    
    for i in range(2, n):
        ary[0][i] += max(ary[1][i-1], ary[1][i-2])
        ary[1][i] += max(ary[0][i-1], ary[0][i-2])
    
    print(max(ary[0][n-1], ary[1][n-1]))