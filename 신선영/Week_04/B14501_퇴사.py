# [BOJ] 14501. 퇴사
import sys
input = sys.stdin.readline

N = int(input())
# 전체 상담 일정
P = [0] + [list(map(int, input().split())) for _ in range(N)]

# 해당 날짜에 끝나는 상담 날짜
E = [[] for _ in range(N + 1)]

# 날짜별 최대 이익
DP = [0]

# 끝나는 날짜 계산
for i in range(1, N + 1):
    idx = P[i][0] + i - 1
    if idx <= N:
        E[idx].append(i)

for i in range(1, N + 1):
    # 현재 날짜에 끝나는 상담이 없는 경우 DP[i - 1]이 최대
    d = DP[i - 1]
    if len(E[i]) > 0:
        # 당일 끝나는 상담을 포함할 경우와 비교
        for e in E[i]:
            d = max(DP[e - 1] + P[e][1], d)
    DP.append(d)

print(DP[N])           