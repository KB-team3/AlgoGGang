# [BOJ] 11052. 카드 구매하기
import sys
input = sys.stdin.readline

N = int(input())  # 카드의 개수
# 카드팩은 1개부터 시작: 인덱스 맞추기 위해 [0] 추가
L = [0] + list(map(int, input().split()))

# 카드 1개부터 구매하기 위한 최대값 기록
DP = [0, L[1]]

for i in range(2, N + 1):
    # i개 들어있는 카드팩 하나만으로 사는 것 기준
    a = L[i]
    for j in range(1, i // 2 + 1):
        # 다른 조합들로 사는 것과 최대값 비교
        a = max(a, DP[j] + DP[i - j])
    DP.append(a)

print(DP[N])