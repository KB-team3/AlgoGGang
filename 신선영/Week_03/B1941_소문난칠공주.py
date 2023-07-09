# [BOJ] 1941. 소문난 칠공주
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque


def check(lst):
    # 7개의 좌표가 서로 연결되어 있는지, S의 수가 4개 이상인지 체크
    cnt = 0
    y = 0

    board = [[0] * 5 for _ in range(5)] # 방문 체크 배열
    board[lst[0][0]][lst[0][1]] = 1  # 시작값 방문 처리

    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # bfs로 탐색
    q = deque()
    q.append(lst[0])
    while q:
        idx = q.popleft()
        ii, jj = idx[0], idx[1]
        cnt += 1

        # Y인지 S인지 확인
        if L[ii][jj] == 'Y':
            y += 1

        if y >= 4:    # y의 수가 4가 되면 (S가 4 이상이 될 수 없으면) 종료
            return "Yexception"

        for k in range(4):
            ni, nj = ii + di[k], jj + dj[k]
            # 범위 체크 + 조합 포함 + 방문 체크
            if 0 <= ni < 5 and 0 <= nj < 5 and [ni, nj] in lst and board[ni][nj] == 0:
                q.append([ni, nj])
                board[ni][nj] = 1  # 방문 처리

    if cnt == 7:
        return True
    else:
        return False


L = [[] for _ in range(5)]
for j in range(5):
    i = input().rstrip()
    for ii in i:
        L[j].append(ii)

P = []   # 5 * 5 배열에서 가능한 좌표값들
for i in range(5):
    for j in range(5):
        P.append([i, j])

C = list(combinations(P, 7))  # 7명이 될 수 있는 모든 좌표의 경우
ans = 0

for c in C:
    if check(c) == True:
        ans += 1

print(ans)
