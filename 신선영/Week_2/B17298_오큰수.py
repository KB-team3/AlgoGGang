# [BOJ] 17928. 오큰수

import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))
T = []  # 현재 가능한 경우의 수 (높은 값들) 저장
A = []  # 정답 저장할 리스트

for i in range(N - 1, -1, -1):  # 마지막부터 탐색
    if len(T) == 0:   # 더 높을 수 있는 경우의 수가 없는 경우 -1
        A.append(-1)
        T.append(L[i])  # 현재 값 후보로 저장

    else:
        while T and T[-1] <= L[i]:  # 더 큰 값을 찾을 때까지 후보 없애버림
            T.pop(-1)
        if T:
            A.append(T[-1])   # 찾으면 마주한 값을 답에 추가
        else:
            A.append(-1)  # 후보중에 더 큰 값이 없으면 -1
        T.append(L[i])  # 현재 내 값도 후보에 부조건 추가

for i in range(N - 1, -1, -1):  # 답 순서 반대로 출력
    print(A[i], end=" ")
