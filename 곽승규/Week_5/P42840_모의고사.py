def solution(answers):
    answer = []
    
    # 각 3인방의 패턴
    user1Pattern = [1,2,3,4,5]
    user2Pattern = [2,1,2,3,2,4,2,5]
    user3Pattern = [3,3,1,1,2,2,4,4,5,5]
    
    # 각 학생이 맞춘 문제 개수 담을 리스트 생성
    ans = [0] * 3
    
    for i in range(len(answers)):
        if user1Pattern[i % 5] == answers[i]:
            ans[0] += 1
        if user2Pattern[i % 8] == answers[i]:
            ans[1] += 1
        if user3Pattern[i % 10] == answers[i]:
            ans[2] += 1
    
    # 학생들 별 몇 문제 맞췄는지 체크
    maxValue = max(ans) # 사람들 중 가장 많이 맞춘 문제 수
    for i in range(3):
        if maxValue == ans[i]:
            answer.append(i+1)
            
    answer.sort()
    return answer

