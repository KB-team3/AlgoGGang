# [BOJ] 13549. 숨바꼭질 3
import sys
input = sys.stdin.readline
from collections import deque


# 최소값 찾기: BFS 사용
def bfs(N):
    v = [0 for x in range(100001)]
    q = deque()
    q.append([N, 0])
    v[N] = 1  # visited 체크 안 하면 메모리 초과

    while q:
        c = q.popleft()
        if c[0] == K:  # K에 도착하면 현재까지의 시간 리턴
            return c[1]

        # 순간이동이 0초로 빠르므로 먼저 순회          
        d = [c[0] * 2, c[0] - 1, c[0] + 1]
        for i in range(3):  # 3개의 경우의 수 (+1, -1, *2)
            # if문에서 인덱스 체크 먼저 -> visited 체크 먼저 할 시 indexError
            if i == 0 and 0 <= d[i] <= 100000 and v[d[i]] == 0:  # 순간이동하는 경우
                v[d[i]] = 1
                q.append([d[i], c[1]])
            elif i in [1, 2] and 0 <= d[i] <= 100000 and v[d[i]] == 0: 
                v[d[i]] = 1
                q.append([d[i], c[1] + 1])  # 1초가 소요되므로 소요시간에 1 추가


# N: 수빈이, K: 동생의 위치
N, K = map(int, input().split())
print(bfs(N))