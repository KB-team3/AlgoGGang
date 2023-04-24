from itertools import combinations
import sys

input = sys.stdin.readline

# N: 도시 크기, M: 최대 치킨집 수
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
ans = sys.maxsize   # 최솟값을 찾는 것이기 때문에 최대로 초기값 설정

h = []  # 전체 집의 좌표
c = []  # 전체 치킨집의 좌표

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            h.append([i + 1, j + 1])
        elif city[i][j] == 2:
            c.append([i + 1, j + 1])

# print(h, c)

for m in range(M, 0, -1):
    # m개부터 1개까지 가능한 모든 치킨집 경우의 수
    lc = list(combinations(c, m))
    for l in lc:  # l: m개의 치킨집 경우
        d = []  # 모든 집의 치킨 거리 누적
        for hh in h:
            hd = []
            for ll in l:
                # 집별로 각 치킨집까지의 거리를 구한다
                hd.append(abs(hh[0] - ll[0]) + abs(hh[1] - ll[1]))
            # 치킨 거리를 구해서 전체 치킨 거리에 포함
            d.append(min(hd))
            # 전체 치킨 거리의 합이 이미 정답 이상인 경우 break
            if sum(d) > ans:
                break
        ans = min(ans, sum(d))


print(ans)
