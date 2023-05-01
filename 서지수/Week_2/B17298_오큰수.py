import sys
input=sys.stdin.readline

N=int(input())
A=(list(map(int, input().split())))

result = [-1] * N
stack = []


stack.append(0)
for i in range(1, N):
    while stack:
        if A[stack[-1]] >= A[i]:
            break
        result[stack.pop()] = A[i]
    stack.append(i)

for i in range(len(result)):
    print(result[i], end=" ")

print()