def time_convert(string):
    h, m = map(int, string.split(":"))
    return h * 60 + m


def solution(book_time):
    answer = 0
    check_change_list = list()
    for start, end in book_time:
        check_change_list.append((time_convert(start), 1))
        check_change_list.append((time_convert(end) + 10, 0))

    check_change_list.sort()

    tmp = 0
    for t, chk in check_change_list:
        tmp += -1 if chk == 0 else 1
        answer = max(answer, tmp)
    return answer