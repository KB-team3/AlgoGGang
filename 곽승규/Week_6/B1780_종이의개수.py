import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 딕셔녀리 생성
dic_a = {-1: 0, 0: 0, 1: 0}

# 입력받기
N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))
# print(paper)


def dfs(x, y, n):
    curr = paper[x][y]  # 종이의 첫 시작 숫자 저장
    for i in range(x, x + n):
        for j in range(y, y + n):
            if curr != paper[i][j]:  # 숫자가 다르면
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return

    if curr == 0:
        dic_a[0] += 1
    elif curr == 1:
        dic_a[1] += 1
    else:
        dic_a[-1] += 1


dfs(0, 0, N)
for i in dic_a.values():
    print(i)
