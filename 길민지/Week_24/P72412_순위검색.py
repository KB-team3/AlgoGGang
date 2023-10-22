from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    
    # info 딕셔너리로 변환
    infos = {}
    for i in info:
        split = i.split()
        keys = split[:-1]
        value = int(split[-1])
        
        # info로 만들 수 있는 모든 조합 생성
        for j in range(5):
            for k in combinations(keys, j):
                key = ' '.join(k)
                if key in infos:
                    infos[key].append(value)
                else:
                    infos[key] = [value]
        
    #infos 점수순 정렬
    for i in infos:
        infos[i].sort()
    
    # query와 비교
    for q in query:
        # 리스트로 변환
        queryList = q.split()
        # and, - 삭제
        while 'and' in queryList:
            queryList.remove('and')
        while '-' in queryList:
            queryList.remove('-')

        queryKey = ' '.join(queryList[:-1])
        queryValue = int(queryList[-1])

        # 쿼리 조건에 맞는 info 개수 세기
        if queryKey in infos:
            values = infos[queryKey]
            if values:
                num = bisect_left(values, queryValue)
                answer.append(len(values)-num)
        else:
            answer.append(0)
        
    return answer