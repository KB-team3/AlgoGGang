def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    i = 0
    for a in A:
        while i<len(B):
            if B[i]>a:
                answer+=1
                i+=1
                break
            i+=1
        
    return answer