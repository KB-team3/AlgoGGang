from itertools import combinations
import copy
def combs(order, n):
    temp = list(combinations(list(order),n))
    answer = []
    for tem in temp:
        st = ''.join(tem)
        answer.append(st)
    return answer
def solution(orders,course):
    answer=[]
    temp=[]
    for order in orders:
        temp.append(sorted(order))
    orders=copy.deepcopy(temp)
    for c in course:
        dicts = {}
        max = 0
        for order in orders:
            for comb in combs(order, c):
                if comb in dicts:
                    dicts[comb]+=1
                else:
                    dicts[comb]=1
        dicts = sorted(dicts.items(),key=lambda x:x[1],reverse=True)
        temp = []
        for dict in dicts:
            if dicts[0][1]==dict[1] and dict[1]!=1:
                answer.append(dict[0])
            else: break
    return sorted(answer)