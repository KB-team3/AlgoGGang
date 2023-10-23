from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        curr = prices.popleft()
        count = 0
        
        for i in prices:
            if curr > i:
                count += 1
                break
            count += 1
        answer.append(count)
    return answer