def solution(name):
    answer = 0
    updown = [min(ord(x) - 65, 91 - ord(x)) for x in name]
    maxL, maxI, cur = 0, 0, 0

    for i, n in enumerate(name):
        if n == "A":
            cur += 1
            if cur > maxL:
                maxI = i
            if cur >= maxL:
                maxL = max(cur, maxL)
            
        else:
            cur = 0
        

    # print("앞: ", maxI - maxL)
    # print("뒤: ", len(name) - maxI - 1)
    
    answer = sum(updown) - maxL + len(name) - 1
        
    return answer
