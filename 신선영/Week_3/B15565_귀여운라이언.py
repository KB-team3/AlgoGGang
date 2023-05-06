# [BOJ] 15565. 귀여운 라이언
import sys
input = sys.stdin.readline

# N: 인형 개수 K: 최소 집합 크기
N, K = map(int, input().split())
L = list(map(int, input().split()))
ans = 10 ** 6  # K의 최대값
c = []  # 라이언 인형의 인덱스 담을 배열

# 전체 인형 중 라이언의 위치만 저장
for i in range(N):
    if L[i] == 1:
        c.append(i)

# 라이언의 개수가 모자란 경우 -1 출력
if len(c) < K:
    print(-1)
else:
    # 라이언의 위치만 저장했기 때문에 현재 인덱스 + K만큼이 라이언 K개를 포함한 집합의 길이가 됨
    for i in range(len(c) - K + 1):
        a = c[i + K - 1] - c[i] + 1
        ans = min(a, ans)
    print(ans)
