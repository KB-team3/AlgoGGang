def solution(survey, choices):
    answer = ''
    
    # 각 성격 유형의 지표 저장 (문제에 정의)
    ind = [{'R': 0, 'T': 0}, {'C': 0, 'F': 0}, {'J': 0, 'M': 0}, {'A': 0, 'N': 0}]
    
    # survey값이 몇 번째 지표에 해당하는지 찾기 위한 인덱스 배열
    idx = ['R', 'C', 'J', 'A']
    
    for i in range(len(survey)):
        # 사전순으로 첫 번째 값과 idx 배열을 이용해 몇 번째 지표인지 찾음
        key = ind[idx.index(sorted(survey[i])[0])]
        if choices[i] <= 3: # 비동의인 경우 0번 인덱스에 해당하는 유형 점수 추가
            key[survey[i][0]] += 4 - choices[i]
        else:   # 동의인 경우 1번 인덱스 유형
            key[survey[i][1]] += choices[i] - 4
    
    for i in ind:   # 4개 지표의 결과를 확인
        for ii in i:    # 알파벳 순서로 되어있기 때문에 둘 중 큰 값에 해당하면 break
            if i[ii] ==  max(i.values()):
                answer += ii
                break
    
    return answer
