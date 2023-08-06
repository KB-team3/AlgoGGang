def solution(n, times):
    answer = 0
    times.sort()
    
    start=1
    end=times[-1]*n
    
    while True:
        if start>end:
            break
        
        middle=(start+end)//2
        
        if sum([middle//x for x in times])>=n:
            end=middle-1
        else:
            start=middle+1
    
    return start