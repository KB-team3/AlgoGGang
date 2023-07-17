def solution(survey, choices):
    score = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0,
    }

    # 점수 계산
    for i in range(len(choices)):
        if(choices[i]<4):
            score[survey[i][0]] += 4-choices[i]
        else:
            score[survey[i][1]] += choices[i]-4

    # 유형 결정
    answer = ''
    answer+= 'R' if score['R'] >= score['T'] else 'T'
    answer+= 'C' if score['C'] >= score['F'] else 'F'
    answer+= 'J' if score['J'] >= score['M'] else 'M'
    answer+= 'A' if score['A'] >= score['N'] else 'N'

    return answer