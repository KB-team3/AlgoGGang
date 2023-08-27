cnt = int(input())

for _ in range(cnt):
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(2)]

    if n > 1:
        M[0][1] += M[1][0]
        M[1][1] += M[0][0]
    for i in range(2, n):
        M[0][i] += max(M[1][i-1], M[1][i-2])
        M[1][i] += max(M[0][i-1], M[0][i-2])
    print(max(M[0][n-1], M[1][n-1]))