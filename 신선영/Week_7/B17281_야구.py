import sys
input=sys.stdin.readline
from itertools import permutations


def play(ord):  # ord: 타순
    ord.insert(3, 0)
    score = 0
    inn = 0  # 현재 이닝
    cur = 0  # 현재 타순
    board = [0, 0, 0]  # 1루, 2루, 3루
    out = 0

    while inn < N:  # 최대 이닝 전까지 진행
        # out 3개 이하인 경우 경기 진행
        # 경기 진행 과정
        res = R[inn][ord[cur]]

        if res == 0:   # 아웃
            out += 1
          
        elif res == 1:  # 안타
            if board[2] == 1:  # 3루에 주자 있는 경우
                score += 1
                board[2] = 0
            if board[1] == 1:  # 2루에 주자 있는 경우
                board[2] = 1
                board[1] = 0
            if board[0] == 1:  # 1루에 주자 있는 경우
                board[1] = 1
                board[0] = 0
            board[0] = 1  # 타자 진루
          
        elif res == 2:  # 2루타 (2, 3루 득점 가능)
            if board[2] == 1:  # 3루에 주자 있는 경우
                score += 1
                board[2] = 0
            if board[1] == 1:  # 2루에 주자 있는 경우
                score += 1
                board[1] = 0
            if board[0] == 1:  # 1루에 주자 있는 경우
                board[2] = 1
                board[0] = 0
            board[1] = 1  # 타자 진루 (2루)
    
        elif res == 3:  # 3루타 (1, 2, 3루 득점 가능)
            if board[2] == 1:  # 3루에 주자 있는 경우
                score += 1
                board[2] = 0
            if board[1] == 1:  # 2루에 주자 있는 경우
                score += 1
                board[1] = 0
            if board[0] == 1:  # 1루에 주자 있는 경우
                score += 1
                board[0] = 0
            board[2] = 1  # 타자 진루 (3루)
    
        elif res == 4:  # 홈런
            if board[2] == 1:
                score += 1
                board[2] = 0
            if board[1] == 1:
                score += 1
                board[1] = 0
            if board[0] == 1:
                score += 1
                board[0] = 0
            score += 1
          
            ''' 이렇게 하면 시간초과
            score += board.count(1) + 1  # 타자 포함 모두 득점
            board = [0, 0, 0]
            '''
    
        

        cur += 1
        if cur == 9:
            cur = 0
            

        # out이 3개 되는 순간 다음 이닝
        if out == 3:
            out = 0
            board = [0, 0, 0]
            inn += 1

    return score
    
    
        

N = int(input())  # 이닝 수 (2 <= N <= 50)
L = permutations([1, 2, 3, 4, 5, 6, 7, 8], 8)

R = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for l in L:
    ans = max(ans, play(list(l)))

print(ans)
