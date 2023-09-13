import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for tc in range(T):
    N = int(input())  # 통나무의 개수
    L = sorted([*map(int, input().split())])
    ans = 0

    q = deque()
    
    for idx, l in enumerate(L):
        if idx % 2:
            q.append(l)
        else:
            q.appendleft(l)

    for i in range(1, N):
        ans = max(ans, abs(q[i] - q[i - 1]))

    print(ans)
