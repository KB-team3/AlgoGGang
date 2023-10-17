import sys
input = sys.stdin.readline

def find(n):
    if link[n] == n:
        return n
    else:
        return find(link[n])

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        link[y] = x
    else:
        link[x] = y

N = int(input())  # 도시의 수
M = int(input())

link = [i for i in range(N + 1)]

for i in range(1, N + 1):
    cur = list(map(int, input().split()))
    for j in range(1, N + 1):
        if cur[j - 1] == 1:
            union(i, j)

ans = "YES"
travel = list(map(int, input().split()))

for i in range(1, M):
    if find(travel[i]) != find(travel[i - 1]):
        ans = "NO"
        break

print(ans)
