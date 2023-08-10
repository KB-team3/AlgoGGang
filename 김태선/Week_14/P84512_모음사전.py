def solution(word) : 
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']

    for i in range(len(word)) : 
        temp = 0
        for j in range(0, 5 - i) : 
            temp += (5 ** j)
        answer += temp * arr.index(word[i]) + 1

    return answer