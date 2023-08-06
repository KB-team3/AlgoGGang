from collections import defaultdict

def solution(tickets):
    answer = []
    path = defaultdict(list)

    # ticket 배열 -> {출발지 : [목적지1, 목적지2, 목적지3 ...]} 형태로 바꿔주기
    for ticket in tickets:
        path[ticket[0]].append(ticket[1])

    # path의 목적지 배열을 역순으로 정렬
    # 맨 뒤부터 stack에 들어가기 때문
    for key in path.keys():
        path[key].sort(reverse=True)

    stack = ['ICN']
    
    # 스택에 원소가 없어질때까지 반복
    while stack:
        # 스택에 제일 마지막에 추가된 목적지
        top = stack[-1]
        
        # 출발지를 top으로 잡은 여행경로가 path에 없는 경우 맨 위의 원소를 answer에 넣어준다.
        if not path[top]:
            answer.append(stack.pop())
        else:
        # 그렇지 않은 경우 스택에 넣음
            stack.append(path[top].pop())

    answer.reverse()

    return answer