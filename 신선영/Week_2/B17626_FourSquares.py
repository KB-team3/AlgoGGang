# [BOJ] 17626. Four Squares  2023-04-27

import sys

N = int(sys.stdin.readline())
L = []  # 1부터 루트N까지 합에 포함될 수 있는 모든 제곱수 리스트

for n in range(1, round(N ** (1/2)) + 2):
    L.append(n * n)

ans = 4   # 최대로 가능한 값은 4

if N in L:  # 처음부터 제곱수인 경우 답은 1
    ans = 1
    
else:   # 인덱스 돌며 2개, 3개로 완성 가능한 경우 답 수정
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[i] + L[j] == N:  
                ans = 2
                break
                
    if ans == 4:  # 답이 1이나 2가 아닌 경우
        for i in range(len(L)):
            for j in range(i, len(L)):
                for k in range(j, len(L)):
                    if L[i] + L[j] + L[k] == N:
                        ans = 3
                        break

print(ans)
