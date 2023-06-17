import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 값 입력받기
N = int(input())
ary = [list(map(int, input().split())) for _ in range(N)]
#print(ary)
c = [1,2,3,4,5,6,7,8] 
orders = permutations(c, 8) # 8개의 원소 중 8개를 뽑아 줄을 세우는 경우!

ans = 0
for o in orders:
    score = 0
    case = list(o)
    case.insert(3,0) # 인덱스 0은(1번선수) 4번타자이므로 여기에 넣기
    #print(case)
    ining = 0 # 이닝
    out = 0 # 아웃카운트
    player = 0
    base = [False, False, False, False]
    while ining < N:
        now_player = case[player]
        now = ary[ining][now_player]
        
        #각 케이스 별로 정하기
        if now == 0: # 아웃
            out += 1
        elif now == 1: # 1루타
            if base[3] == True:
                score += 1
                base[3] = False
            if base[2] == True:
                base[2] = False
                base[3] = True
            if base[1] == True:
                base[1] = False
                base[2] = True
            base[1] = True
        elif now == 2: # 2루타
            if base[3]==True:
                score+=1
                base[3]= False
            if base[2]==True:
                base[2]=False
                score+=1
            if base[1]==True:
                base[1]=False
                base[3]=True
            base[2]=True
        elif now == 3: #3루타
            if base[3]== True:
                score+=1
                base[3]=False
            if base[2]== True:
                base[2]=False
                score+=1
            if base[1]==True:
                base[1]=False
                score+=1
            base[3]=True
        #홈런
        elif now == 4:
            if base[3]==True:
                score+=1
                base[3]= False
            if base[2]== True:
                base[2]=False
                score+=1
            if base[1]==True:
                base[1]= False
                score+=1
            score+=1
        
        player = (player + 1) % 9 # 플레이어 다음 사람으로 바꾸기 (9명이 최대이므로 계속 돌도록함)
        
        if out == 3: # 3아웃이면 초기화
            ining += 1
            base = [False, False, False, False]
            out = 0
    ans = max(ans, score)

print(ans)