import sys

input=sys.stdin.readline

N, M=map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

# print(N, M, A)

result=arr[N-1][M-1]
i=N-1
j=M-1

while(1):
    if i==0 and j!=0:
        num1=0
        num2=arr[i][j-1]
        num3=0
    elif i!=0 and j==0:
        num1=arr[i-1][j]
        num2=0
        num3=0
    elif i==0 and j==0:
        break
    elif i!=0 and j!=0:
        num1=arr[i-1][j]
        num2=arr[i][j-1]
        num3=arr[i-1][j-1]

    result+=max(num1, num2, num3)

    if max(num1, num2, num3)==num1:
        i=i-1
        j=j
    elif max(num1, num2, num3)==num2:
        i=i
        j=j-1
    elif max(num1, num2, num3)==num3:
        i=i-1
        j=j-1
        

print(result)
