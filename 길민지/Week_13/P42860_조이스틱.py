def solution(name):
    answer = 0
    A = ord('A')
    Z = ord('Z')
    
    alphabet = 0
    start = 0
    end = -1
    cnt = 0
    maxCnt = 0
    maxStart = 0
    maxEnd = -1
    check = False
    cursor = len(name)-1
    
    for i in range(len(name)):
	# 연속 A 체크
        if name[i]=='A':
            if check == False:
                check = True
                start = i
                cnt = 0
            end = i
            cnt += 1
            
            if(maxCnt<cnt):
                maxCnt = cnt
                maxStart = start
                maxEnd = end
            continue
        # 알파벳 체크
        check = False
        num = ord(name[i])   
        alphabet += min(num-A, Z-num+1)
    if (maxCnt > 0) :
        forward = 0 if maxStart==0 else maxStart - 1
        backward = len(name) - maxEnd - 1
        fb = min(forward, backward) + forward + backward
        cursor = min(cursor, fb)
        
    return alphabet + cursor