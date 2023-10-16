def solution(prices):
    answer = [0]*len(prices)
    stack = []
    
    for i in range(len(prices)):
        if len(stack) == 0: # 스택이 비었을 경우 값 추가
            stack.append([prices[i], i, 0]) # 값, 위치, 카운트
        else:
            # 1초 증가
            for j in range(len(stack)):
                stack[j][2] += 1
            # 가격이 떨어진 값 제거
            while len(stack) != 0 and stack[-1][0]>prices[i] :
                pop = stack.pop()
                answer[pop[1]] = pop[2]
            # 스택에 해당 값 추가
            stack.append([prices[i], i, 0]) 
            
    # 남은 스택도 정답 리스트에 추가
    for i in range(len(stack)):
        answer[stack[i][1]] = stack[i][2]
        
    return answer