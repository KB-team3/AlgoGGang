import sys

input=sys.stdin.readline

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
temp = [0] * n

for i in range(n):
    # 키 큰 사람 수
    cnt = 0 

    for j in range(n):
        if cnt == arr[i] and temp[j] == 0:
            temp[j] = i + 1
            break
        elif temp[j] == 0:
            cnt += 1

for t in temp:
    print(t, end=" ")
