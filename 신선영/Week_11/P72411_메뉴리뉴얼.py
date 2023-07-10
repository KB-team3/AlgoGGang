from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    
    for c in course:
        dict = defaultdict(int)
        for o in orders:
            # 가능한 메뉴의 조합
            comb = list(combinations(o, c))
            for cc in comb:
                # sort하지 않으면 순서가 다른 조합을 같은 것으로 인지하지 못함
                dict[''.join(sorted(cc))] += 1
        maxa = 0
        a = []     
        for k, v in dict.items():
            if v >= 2:
                if v > maxa:
                    a = [k]
                    maxa = v
                elif v == maxa:
                    a.append(k)
        for aa in a:
            answer.append(aa)
    
    return sorted(answer)
