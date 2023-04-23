import sys
input=sys.stdin.readline


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

isVisited=[]
for i in range(N):
    for j in range(N):
        isVisited[i][j]=False;

# print(N, M, graph)


