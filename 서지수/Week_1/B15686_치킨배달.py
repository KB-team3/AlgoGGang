import sys
import itertools
input=sys.stdin.readline


N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

home=[]
chicken=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1:
            home.append([i, j]) # 집 좌표 저장
        elif graph[i][j]==2:
            chicken.append([i,j]) # 치킨집 좌표 저장

# distance=[[] for _ in range(len(home))]

# print(distance)
# print(home)
# print(chicken)

# for i in range(len(home)):
#     for j in range(len(chicken)):
#         distance[i].append(abs(home[i][0]-chicken[j][0])+abs(home[i][1]-chicken[j][1])) # 각 집과 치킨집마다의 치킨 거리 

# print(distance)


# 최대 M개니까, 총 치킨집에서 M개를 뽑는 조합
nCr = itertools.combinations(chicken, M);
# print(list(nCr))
result = 10000000
for chick in nCr:  
    temp = 0            # 모든 치킨 거리
    for i in range(len(home)): 
        chi_len = 10000   # 각 집과 치킨집마다의 치킨 거리
        for j in range(M):
            chi_len = min(chi_len, abs(home[i][0] - chick[j][0]) + abs(home[i][1] - chick[j][1]))
        temp += chi_len
    result = min(result, temp)

print(result)