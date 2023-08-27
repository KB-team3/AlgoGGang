import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input()) # 포도주 잔 개수

# 입력받기
podo = [0]
for i in range(N):
    podo.append(int(input()))

podo.append(0) # N이 1일 경우 처리

dp = [0] * 10001

# 초기 설정해놓기
dp[1] = podo[1]
dp[2] = podo[1] + podo[2]

for i in range(3, N+1):   
    # i번째 잔 마셨을 때 선택할 수 있는거
    dp[i] = max(dp[i-3] + podo[i-1] + podo[i], dp[i-2] + podo[i])
 
    # 계단오르기와 달리 i번째 잔 안먹을 수도 있음
    # 그러면 dp[i]는 곧 dp[i-1]임
    # 그래서 둘 중 큰 걸 고르는 것임
    dp[i] = max(dp[i], dp[i-1])

print(dp[N])