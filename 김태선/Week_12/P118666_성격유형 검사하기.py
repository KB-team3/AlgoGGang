def solution(survey, choices) : 
    answer = ''
    N = len(survey)
    personality = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}

    # 성격유형은 key, 점수는 value로 딕셔너리 작성
    # 문제 설명대로 구현
    for i in range(N) : 
        # mbti 성격유형의 경우 두가지 결과를 나타나므로 f, s 변수 생성
        first, second = survey[i][0], survey[i][1]
        if choices[i] <= 3 : 
            personality[first] += 4 - choices[i]
        elif choices[i] > 4 :  
            personality[second] += choices[i] - 4
    
    if personality['R'] >= personality['T'] : 
        answer += 'R'
    else : 
        answer += 'T'

    if personality['C'] >= personality['F'] : 
        answer += 'C'
    else : 
        answer += 'F'

    if personality['J'] >= personality['M'] : 
        answer += 'J'
    else : 
        answer += 'M'

    if personality['A'] >= personality['N'] : 
        answer += 'A'
    else : 
        answer += 'N'

    return answer