def solution(n, times):
    answer = 0
    start = 0
    # 가장 오래 걸리는 시간
    end = max(times) * n

    while start <= end : 
        mid = (start + end) // 2
        # 모든 심사관들이 mid분 동안 심사한 사람의 수
        people = 0
        
        for time in times : 
            people += mid // time
        # 처리하는 인원 수가 n과 같거나 큰 경우, mid 줄임
        if n <= people : 
            end = mid - 1
        else : 
            start = mid + 1
    
    answer = start
    return answer