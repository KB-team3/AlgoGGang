import sys
input=sys.stdin.readline

N=int(input())
P=(list(map(int, input().split())))

dp=[0]

for i in range(1, N+1):
    if 4%i==0: # 나누어 떨어진다면 P[i]에서 곱해지면 됨
        dp.append(int(P[i-1]*(N/i)))
    else: # 나누어 떨어지지 않으면 다른 값을 더해주어야함
        dp.append(int(P[i-1]+P[N-i-1]))

print(max(dp))