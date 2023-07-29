from collections import defaultdict


def solution(tickets):
    answer = ["ICN"]
    # 키 : 출발지, 값 : 도착지
    route = defaultdict(list)

    for ticket in tickets : 
        route[ticket[0]].append(ticket[1])

    # 값을 기준으로 역순으로 정렬
    for key in route.keys() : 
        route[key].sort(reverse = True)
    
    stack = ["ICN"]
    path = []

    while stack : 
        # 스택 가장 위의 값 데이터
        top = stack[-1]

        # top이 그래프에 없거나, top을 시작점으로 하는 티켓이 없는 경우
        if not route[top] or len(route[top]) == 0 : 
            path.append(stack.pop())
        else : 
            stack.append(route[top].pop())
    # path 역순
    path.reverse()
    return path