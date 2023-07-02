# [BOJ] 2564. 경비원

import sys
input = sys.stdin.readline

h, v = map(int, input().split())  # 가로, 세로 길이
n = int(input())  # 상점의 개수
S = []
ans = 0

# 1: 위, 2: 아래, 3: 왼, 4: 오
for _ in range(n):
    S.append(list(map(int, input().split())))

d1, d2 = map(int, input().split())

for s in S:
    if d1 == 1:
        if s[0] == 4:
            ans += h - d2 + s[1]
        elif s[0] == 3:
            ans += d2 + s[1]
        elif s[0] == 2:
            ans += min(d2 + v + s[1], h - d2 + v + h - s[1])
        elif s[0] == 1:
            ans += abs(d2 - s[1])
    
    elif d1 == 2:
        if s[0] == 4:
            ans += h - d2 + v - s[1]
        elif s[0] == 3:
            ans += d2 + v - s[1]
        elif s[0] == 1:
            ans += min(d2 + v + s[1], h - d2 + v + h - s[1])
        elif s[0] == 2:
            ans += abs(d2 - s[1])
        
    elif d1 == 3:
        if s[0] == 1:
            ans += d2 + s[1]
        elif s[0] == 2:
            ans += v - d2 + s[1]
        elif s[0] == 4:
            ans += min(d2 + h + s[1], v - d2 + h + v - s[1])
        elif s[0] == 3:
            ans += abs(d2 - s[1])
    
    else:
        if s[0] == 1:
            ans += d2 + h - s[1]
        elif s[0] == 2:
            ans += v - d2 + h - s[1]
        elif s[0] == 3:
            ans += min(d2 + h + s[1], v - d2 + h + v - s[1])
        elif s[0] == 4:
            ans += abs(d2 - s[1])

print(ans)
