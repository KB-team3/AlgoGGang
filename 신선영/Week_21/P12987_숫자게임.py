def solution(A, B):
    answer = 0
    L, i, j = len(A), 0, 0
    A.sort()
    B.sort()
    
    while j < L:
        # 이길 수 있는 경우
        if A[i] < B[j]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1
        
    return answer
