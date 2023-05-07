import sys
input=sys.stdin.readline

N, K=map(int, input().split())
dolls=list(map(int,input().split()))

min_value=1000000

for start in range(N):
    sum=0 # 1의 개수
    end=start
    cnt=0 # 1을 K개 포함한 연속된 집합의 크기
    while end<N:
        if sum==K:
            break
        if dolls[end]==1:
            sum+=1
        end+=1
        cnt+=1
    if sum==K and min_value>cnt:
        min_value=cnt

if min_value==1000000:
    min_value=-1

print(min_value)