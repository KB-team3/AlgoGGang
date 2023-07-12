import itertools

N, K = map(int, input().split())

products = []
for i in range(N):
    w, h = map(int, input().split())
    products.append([w,h])

max_value = 0
for num in range(1, N+1):
    res = itertools.combinations(products, num)
    comb = list(res)
    # print("comb:", comb)
    case_sum = 0
    for case in comb: #다음 경우
        # print("case:", case)
        flag = 1
        w_sum = 0
        v_sum = 0
        for ele in case:
            w_sum += ele[0]
            v_sum += ele[1]
            if w_sum > K:
                flag = 0
                break
        if flag == 1:
            case_sum = max(case_sum, v_sum)
            # print("case_sum:", case_sum)
    # print("case_sum:", case_sum)
    max_value = max(max_value, case_sum)
print(max_value)



