def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    idx1, idx2, idx3 = 0, 0, 0
    cnt = [0, 0, 0] # 각 학생별 맞은 개수 저장
    
    for a in answers:
        # 만약 답과 학생의 현재 찍은 값이 갔다면 맞은 개수 추가
        if s1[idx1] == a:
            cnt[0] += 1
        if s2[idx2] == a:
            cnt[1] += 1
        if s3[idx3] == a:
            cnt[2] += 1
        idx1 += 1
        idx2 += 1
        idx3 += 1
        # 한바퀴를 다 돌았을 경우 초기화
        if idx1 == len(s1):
            idx1 = 0
        if idx2 == len(s2):
            idx2 = 0
        if idx3 == len(s3):
            idx3 = 0
        
    m = max(cnt)
    # 가장 많은 개수를 맞힌 학생 모두 answer에 추가
    for i in range(3):
        if cnt[i] == m:
            answer.append(i + 1)
    return answer