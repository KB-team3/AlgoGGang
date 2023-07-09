import sys
input = sys.stdin.readline

N, K = map(int, input().split())
L = list(map(int, input().split()))

s = sum(L[:K])  # 초기값: 첫날부터 K일까지의 합으로 설정
ans = s

# 하루씩 지나갈때마다 다음 날짜 추가, 이전 날짜 삭제 후 값 비교
for i in range(K, N):
    s -= L[i - K]
    s += L[i]

    ans = max(ans, s)

print(ans)
