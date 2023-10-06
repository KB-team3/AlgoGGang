from itertools import permutations

def solution(k, dungeons):
    def exp(order, k):
        cur = k
        cnt = 0

        for o in order:
            n, c = dungeons[o][0], dungeons[o][1]
            if cur >= n:    # 탐험이 가능한 경우
                cur -= c
                cnt += 1
            else: return cnt
            
        return cnt
    
    answer = -1
    orders = [x for x in range(len(dungeons))]
    # 가능한 모든 탐험 순서 경우의 수
    cases = list(permutations(orders, len(dungeons)))
    
    for c in cases:
        answer = max(answer, exp(c, k))
        
    return answer
