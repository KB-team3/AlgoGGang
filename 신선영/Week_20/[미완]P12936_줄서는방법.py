def solution(n, k):
    
    def lineup(idx):
        global cnt, answer
        if idx == n:
            cnt += 1
            if cnt == k:
                answer = selected
                return
            return

        for i in range(n):
            if isSelected[i]:
                continue
            isSelected[i] = 1
            if cnt < k:
                selected[idx] = i + 1
                lineup(idx + 1)
                isSelected[i] = 0
            else:
                return

    global answer
    global cnt
    answer = []
    cnt = 0
    people = [x for x in range(1, n + 1)]
    selected = [0] * n
    isSelected = [0] * n
    
    lineup(0)

    return answer
    
    
    
