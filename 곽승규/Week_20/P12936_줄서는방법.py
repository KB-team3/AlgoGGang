import math

def solution(n, k):
    answer = []
    ary = [i for i in range(1, n+1)]
    k = k - 1 # ex) n = 3, k = 6이면 k // (n-1)! 하면 3이 나옴. 그럼 빼줘야함. k-1로 하면 index와 바로 매칭 가능
    
    result = []
    while ary:
        a = k // math.factorial(n-1) # 즉, k-1에 1도막의 수를 나누는 것임.
        result.append(ary[a])
        del ary[a]
        
        # k 줄이기
        k = k % math.factorial(n-1)
        n -= 1
    
    
    return result