import itertools

weights = [100,180,360,100,270];

def solution(weights):
    answer = 0
    weights = sorted(weights)
    ratios = [1/1, 1/2, 2/3, 3/4]

    res = itertools.combinations(weights, 2)
    comb = list(res)
    # test 출력
    print("comb", comb)

    for case in comb:
        w1, w2 = case
        if w1/w2 in ratios:
            answer += 1
    # test 출력
    print("answer", answer)
    return answer

solution(weights)