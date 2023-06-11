from sys import stdin
from itertools import permutations

read = stdin.readline

# n = 이닝 수
n = int(read()) 

# 이닝별 결과 입력값
inning = [list(map(int, read().split())) for _ in range(n)]
ans = 0

# 순서 permutation 생성
for turn in permutations(range(1, 9)) : 
    order = list(turn[:3]) + [0] + list(turn[3:])
    score = 0
    index = 0  

    for i in range(n) :
        
        #아웃, 1루, 2루, 3루
        out, b1, b2, b3 = 0, 0, 0, 0

        #진짜 야구처럼 쓰리아웃 될때까지
        while out < 3 :
            hit = inning[i][order[index]]
            if hit == 0 :   #아웃
                out += 1
            elif hit == 1 :
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif hit == 2 : 
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif hit == 3 :
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0 , 1
            else : 
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            
            #다음타자로 변경
            index = (index + 1) % 9
    
    ans = max(ans, score)

print(ans)