def solution(info, query):
    newInfo =[]
    answer = []
    for i in info:
        newInfo.append(i.split(' '))
    l = len(info)

    for q in query: # 조건 하나씩 탐색
        que = q.split(' and ')
        temp = que[-1].split(' ')
        que.append(temp[0])
        que.append(temp[1])
        que.pop(-3)
        check = []
        for qq in que:
            if qq == '-':
                check.append(0)
            else:
                check.append(1)
        
        idx = [1 for _ in range(l)]
        for j in range(l):  # 인덱스 하나씩 탐색
            if int(que[4]) > int(newInfo[j][4]):
                idx[j] = 0
                continue
            for i in range(4):
                if check[i] == 1: 
                    # 전체 허용이 아닌데 값이 다르면
                    if newInfo[j][i] != que[i]:
                        idx[j] = 0
                        break
            
        answer.append(idx.count(1))
        
        
    return answer
