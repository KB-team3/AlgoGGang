def solution(tickets):
    # DFS: 재귀 (인덱스 사용?)
    # 순서대로 탐색하면서 [0]이 [1]과 같다면 append

    def travel(i, v, l):
        global check
        if check == 1:
            return 
        
        if len(l) == len(tickets) and 0 not in v:
            l.append(tickets[i][1])
            answer.append(list(l))
            check = 1
            return

        for j in range(len(tickets)):
            if v[j] == 0 and tickets[j][0] == tickets[i][1]:
                l.append(tickets[j][0])
                v[j] = 1
                travel(j, v, l)
                v[j] = 0
                l.pop(-1)


    answer = []
    global check
    check = 0
    tickets = sorted(tickets)	# 알파벳 순서 빠른대로 탐색해야됨
    for idx, t in enumerate(tickets):
        if check:
            break
        if t[0] == "ICN":	# 인천공항에서 출발하는 경우 모두 탐색
            visited = [0] * len(tickets)
            lst = ["ICN"]	# 시작점 저장
            visited[idx] = 1
            travel(idx, visited, lst)
                
    return answer[0]
