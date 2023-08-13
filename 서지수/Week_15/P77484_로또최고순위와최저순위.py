def solution(lottos, win_nums) :
    numbers = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = []
    cnt = 0

    for value in lottos :
        if value in win_nums :
            cnt += 1

    answer.append(numbers[cnt + lottos.count(0)]) # 최고 개수
    answer.append(numbers[cnt])

    return answer