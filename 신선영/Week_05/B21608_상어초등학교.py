# [BOJ] 21608. 상어 초등학교
import sys
input = sys.stdin.readline

# 각 자리별 인접 자리를 구하기 위한 함수
def findclose(i, j):
    global close, maxl, maxseat
    seats = []
    for r in range(N):
        for c in range(N):
            if abs(i - r) + abs(j - c) == 1:
                  seats.append([r, c])
                    
    # 인접 조건에 맞는 값들을 close의 해당 위치에 모아두기
    close[i][j] = seats
    # 첫 학생의 자리를 구하기 위해 인접 자리가 가장 많은 값도 구해둠
    if len(seats) > maxl:
        maxl = len(seats)
        maxseat = [i, j]
    return
      
# 각 학생 별 맞는 자리를 찾기 위한 함수
def findseat(stu, like):
    global close
    # 각 자리 별 좋아하는 친구의 수, 비어있는 인접 자리의 수를 구하기 위한 배열
    seatinfo = [[[0, 0]] * N for _ in range(N)]
    maxl, maxe = 0, 0
    for i in range(N):
        for j in range(N):
            # 현재 비어 있는 자리만 대상으로 확인
            if seated[i][j] == 0:
                l, e = 0, 0
                for c in close[i][j]:
                    # 인접한 자리 중에 좋아하는 친구가 있음
                    if board[c[0]][c[1]] in like:
                        l += 1
                    # 인접한 자리가 비어 있음
                    if board[c[0]][c[1]] == 0:
                        e += 1
                # 이후 사용 위해 좋아하는 친구가 가장 많은 자리의 친구 수와, 비어있는 자리의 max값 저장
                maxl = max(maxl, l)
                maxe = max(maxe, e)
                seatinfo[i][j] = [l, e]

    # 조건 1. 친구가 가장 많은 값을 찾자
    maxlike = []
    for i in range(N):
        for j in range(N):
            if seatinfo[i][j][0] == maxl:
                maxlike.append([i, j])
    if len(maxlike) == 1:    # 친구가 가장 많은 자리가 하나이면 바로 return
        return maxlike[0]

    maxee = 0
    maxempty = []
    # 좋아하는 친구의 수가 같은 자리끼리 비어있는 수 비교
    for m in maxlike:
        if seatinfo[m[0]][m[1]][1] > maxee:
            maxee = seatinfo[m[0]][m[1]][1]
            maxempty = [[m[0], m[1]]]
        elif seatinfo[m[0]][m[1]][1] == maxee:
            maxempty.append([m[0], m[1]])
    if len(maxempty) == 1:
        return maxempty[0]
    
    # 그래도 결과가 나오지 않는 경우 행, 열이 가장 작은 자리 찾기
    for m in maxempty:
        if seatinfo[m[0]][m[1]] != [0, 0]:
            return m
        
    # 처음부터 인접 자리에 좋아하는 친구가 한 명도 없었던 경우
    for i in range(N):
        for j in range(N):
            if seated[i][j] == 0:
                return [i, j]
    

N = int(input())  # 학생의 수

L = [list(map(int, input().split())) for _ in range(N ** 2)]

board = [[0] * N for _ in range(N)]
close = [[[]] * N for _ in range(N)]
seated = [[0] * N for _ in range(N)]

maxl = 0
maxseat = []

# 각 자리에 해당하는 인접값들을 모두 구해 둠
for i in range(N):
    for j in range(N):
        findclose(i, j)

# 첫번째 학생의 자리 정하기
board[maxseat[0]][maxseat[1]] = L[0][0]
seated[maxseat[0]][maxseat[1]] = 1

# 두 번째 학생부터 자리 정하고 seated true 처리
for i in range(1, N ** 2):
    stu = L[i][0]
    like = L[i][1:5]
    idx = findseat(stu, like)
    board[idx[0]][idx[1]] = stu
    seated[idx[0]][idx[1]] = 1

answer = 0

# 만족도 구하기
for n in range(N ** 2):
    stu = L[n][0]
    like = L[n][1:5]
    seat = []
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == stu:
                seat = [i, j]
    c = close[seat[0]][seat[1]]
    for cc in c:
        if board[cc[0]][cc[1]] in like:
            cnt += 1
    if cnt != 0:
        answer += 10 ** (cnt - 1)

print(answer)