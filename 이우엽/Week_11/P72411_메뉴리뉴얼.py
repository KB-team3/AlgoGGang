import itertools
def solution(orders, course):
    dict = {}
    for order in orders:
        order_list = list(order)
        # print("order_list:", order_list)
        for num in course:
            res = itertools.combinations(order_list, num)
            comb = list(res)
            # print(num, "comb:", comb)
            for case in comb:
                case_list = list(case)
                case_list.sort()
                # print("case:", case_list)
                order_str = "".join(case_list)
                # print("sorted_str:", order_str)
                if order_str in dict:
                    dict[order_str] += 1
                else:
                    dict[order_str] = 1
        # print("dict:", dict)
        # dict sort by order 주문 횟수, 주문길이, reverse
    sorted_dict = sorted(dict.items(), key = lambda item: (-len(item[0]), -item[1]))
    # print("sorted_dict:", sorted_dict)
    num = len(sorted_dict[0][0])
    answer = []
    max = 2
    for i, order in enumerate(sorted_dict):
        if len(order[0]) == num:
            if order[1] >= max:
                max = order[1]
                answer.append(order[0])
            else:
                if i == len(sorted_dict)-1:
                    break
                num = len(sorted_dict[i+1][0])
    # print("answer:", answer)
    sorted_answer = sorted(answer, key = lambda x: (x[0], x[1], len(x)))
    print(sorted_answer)
    return sorted_answer