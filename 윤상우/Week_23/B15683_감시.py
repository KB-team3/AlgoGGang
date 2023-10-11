import copy

N,M=map(int, input().split())
graph=[list(map(int, input().split())) for _ in range(N)]
answer=int(1e9)
dx=(0,-1,0,1)
dy=(1,0,-1,0)

# 사방탐색에서 방향이 주어지면 배열로 관리한다.
mode=[
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]
# cctv별로 경우의 수가 다르다. + cctv 하나 당 하나의 경우의 수를 적용 -> 깊이 탐색 (선택하고, 선택하고, ... 마지막까지 선택 이런 느낌)
cctv=[]

for i in range(N):
    for j in range(M):
        if graph[i][j] in [1,2,3,4,5]:
            cctv.append([graph[i][j],i,j])

def dfs(depth, arr):
    # 정답은 전역변수로 관리
    global answer
    if depth==len(cctv):
        # 마지막 cctv의 경우의 수까지 적용된 arr배열에서 사각지대 개수 = count
        count=0
        for row in arr:
            count+=row.count(0)
        # 최솟값 갱신
        answer=min(answer, count)
        return
    
    # 현재 cctv에 대한 정보
    cctv_num,x,y=cctv[depth]
    # arr의 값을 계속해서 copy해서 갱신 -> copy.deepcopy()
    temp=copy.deepcopy(arr)
    
    for m in mode[cctv_num]:
        # 현재 cctv의 방향 하나에 대한 기록
        for i in m:
            nx=x
            ny=y
            # 선택 방향으로 쭉 감시
            while(True):
                nx+=dx[i]
                ny+=dy[i]
                # 벽을 만나거나, 범위를 벗어나면 while문 종료
                if nx<0 or nx>=N or ny<0 or ny>=M or temp[nx][ny]==6 : break
                if temp[nx][ny]==0:
                    temp[nx][ny]=7
        # 다음 cctv로 이동 + temp 배열 가지고 가기
        dfs(depth+1,temp)
        # 임시 배열 초기화 (백트래킹)
        temp=copy.deepcopy(arr)

dfs(0,graph)
print(answer)