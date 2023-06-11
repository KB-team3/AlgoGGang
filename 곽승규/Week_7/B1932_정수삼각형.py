import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 입력값받기
N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(i+1):
        if j == 0: # 삼각형에서 맨 왼쪽
            ary[i][0] += ary[i-1][0]
        elif j == i: # 삼각형에서 맨 오른쪽
            ary[i][j] += ary[i-1][j-1]
        else: # 그 나머지
            ary[i][j] += max(ary[i-1][j-1], ary[i-1][j])

print(max(ary[N-1])) # 마지막 행에서 가장 큰 값 출력하기