# 작성자 : 서지수
# 문제 : B2559_수열

import sys
input=sys.stdin.readline

N, K = map(int, input().split())
graph=(list(map(int, input().split())))
graph.insert(0,0)

#print(N, K, graph)

result=[] # K일의 온도의 합 모음
tmp=[] # graph 누적합

tmp.append(0);
for i in range(1,len(graph)):
    tmp.append(tmp[i-1]+graph[i]);

for j in range(K,N+1):
    result.append(tmp[j]-tmp[j-K]); # 누적합의 뺄셈으로 합 구하기

print(max(result))