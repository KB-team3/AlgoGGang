from sys import stdin
input = stdin.readline

t = int(input())

for i in range(t) : 
    n = int(input())
    log = list(map(int, input().split()))
    # 오름차순 정렬
    log.sort()

    # 높이 차 최댓값
    res = 0
    for j in range(2, n) :
        res = max(res, abs(log[j] - log[j - 2]))

    print(res)
    