import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input()) # 학생의 수는 N**2임
room = [[0]*(N+1) for _ in range(N+1)]
result = 0 # 정답

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 입력값 받기
listA = [list(map(int, input().split())) for _ in range(N**2)]
# print(listA)

for i in range(N**2):
    student = listA[i] # ex ->[2, 1,3,4,5]
    tmp = []
    for r in range(1, N+1):
        for c in range(1, N+1):
            if room[r][c] == 0: # 우선 빈자리 찾아야 함
                like = 0
                empty = 0
                for k in range(4): # 빈자리에서 인접한 곳 탐색
                    nr = r + dr[k]
                    nc = c + dc[k]
                    if nr >= 1 and nr <= N and nc >= 1 and nc <= N:
                        if room[nr][nc] in student[1:]: # 빈 자리 인접 상하좌우에 자신과 친한 친구가 있으면
                            like += 1
                        if room[nr][nc] == 0: # 인접 상하좌우에 빈 자리가 있다면
                            empty += 1
                tmp.append([like, empty, r, c]) # like : 자신이 좋아하는 학생들 수, empty : 빈공간 수, r : 행, c : 열
    tmp.sort(key= lambda x : (-x[0], -x[1], x[2], x[3])) # like, empty는 내림차순! 행, 열은 오름차순!정렬
    room[tmp[0][2]][tmp[0][3]] = student[0] # 정렬했으니 tmp 첫 리스트 행,열에 학생 앉히기
    #print(tmp)
    
# print("room", room) # 확인함

# 학생들 만족도 구하기
listA.sort()

for i in range(1, N+1):
    for j in range(1, N+1):
        count = 0
        # 인접한 곳에 친한친구 몇명 있는지 확인하기
        for k in range(4):
            nr = i + dr[k]
            nc = j + dc[k]
            if nr >= 1 and nr <= N and nc >= 1 and nc <= N:
                if room[nr][nc] in listA[room[i][j]-1]:
                    count += 1
        if count == 0:
            result += 0
        elif count == 1:
            result += 1
        elif count == 2:
            result += 10
        elif count == 3:
            result += 100
        else:
            result += 1000

print(result)
            
