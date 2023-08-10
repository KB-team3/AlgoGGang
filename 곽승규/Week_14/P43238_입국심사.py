def solution(n, times):
    answer = 0
    start, end = 1, max(times) * n
    answer = end
    
    while start <= end:
        mid = (start + end) // 2
        
        people = 0
        for time in times:
            people += (mid // time)
        
        if people < n:
            start = mid + 1
        else:
            end = mid - 1
            answer = min(answer, mid)
        
    return answer