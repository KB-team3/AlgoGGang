N=int(input())
M=int(input())

parent=[i for i in range(N+1)]

def find(n):
    if parent[n]==n:
        return n
    return find(parent[n])

def union(n1,n2):
    n1=find(n1)
    n2=find(n2)

    if n1<=n2:
        for i in range(N+1):
            if parent[i]==n2:
                parent[i]=n1
    else:
        for i in range(N+1):
            if parent[i]==n1:
                parent[i]=n2

for i in range(N):
    temp=list(map(int, input().split()))
    for j in range(N):
        if temp[j]==1:
            union(i+1,j+1)

travel=list(map(int, input().split()))
len = len(travel)

for i in range(len-1):
    if parent[travel[i]]!=parent[travel[i+1]]:
        print('NO')
        exit()

print('YES')