# [BOJ] 2212. 센서

import sys
input = sys.stdin.readline

N = int(input())  # 센서의 개수
K = int(input())  # 집중국의 개수

# 센서의 위치는 중복 가능하기때문에 set 사용
sensors = list(sorted(set(map(int, input().split()))))

L = len(sensors)

# 센서 사이의 거리 값 기록
gaps = sorted([sensors[x + 1] - sensors[x] for x in range(L - 1)])

# 센서 사이의 값 중 가장 큰 K - 1 개를 제거하면 최소 거리의 합과 같음
print(sum(gaps[:L - K]))
