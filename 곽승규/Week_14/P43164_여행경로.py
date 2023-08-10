from collections import defaultdict

def solution(tickets):
    answer = []
    # 인접리스트 생성
    def init():
        route = defaultdict(list)
        for key, value in tickets:
            route[key].append(value)
        return route
    
    def dfs():
        stack = ['ICN']
        path = []
        while len(stack) > 0: # 스택이 빌때까지
            top = stack[-1]
            # top 위치에서 출발하는 티켓이 없거나 티켓을 다 썼을 때
            if top not in route or len(route[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(route[top].pop(0))
        return path[::-1] # 거꾸로 출력
    
    route = init()
    for r in route:
        route[r].sort()
    answer = dfs()
        
    return answer