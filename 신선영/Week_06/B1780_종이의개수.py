# [BOJ] 1780. 종이의 개수
import sys
input = sys.stdin.readline


def cut(i, j, n):
    curN = L[i][j]  # 시작점의 값
    for ii in range(i, i + n):
        for jj in range(j, j + n):
            if L[ii][jj] != curN:
                # 아닌 부분을 만나면 무조건 3분할
                for x in range(3):
                    for y in range(3):
                        cut(i + x * (n // 3), j + y * (n // 3), n // 3)
                return
    ans[curN + 1] += 1
    

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

ans = [0, 0, 0]   # -1, 0, 1
cut(0, 0, N)

for a in ans:
    print(a)
