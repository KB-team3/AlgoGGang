from itertools import combinations


def solution(orders, course):
    answer = []
    menus = {}

    for c in course:
        for o in orders:
            menu = list(combinations(o, c)) # 조합
            for i in menu:
                menus[''.join(sorted(i))] = 0

    # 주문 횟수 세기
    for menu in menus:
        for o in orders:
            if set(list(menu)).issubset(set(list(o))):
                menus[menu] += 1

    # 주문 2번 미만 탈락
    newMenu = []
    for k, v in menus.items():
        if v >= 2:
            newMenu.append((k, v))

    # 최댓값
    possible = []  # 각 코스 갯수에 따른 메뉴 후보군
    possible_ = []
    for c in course:
        for k, v in newMenu:
            if len(k) == c:
                possible.append((k, v))
            else:
                continue
        possible = sorted(possible, key=lambda x: x[1], reverse=True)

        if possible:  # max 값 골라내기
            max_ = possible[0][1]

        for p in possible:  # 최종 값 골라내기
            if p[1] == max_:
                possible_.append(p)
        possible = []

    # 답안 출력
    possible_ = sorted(possible_)
    for a in possible_:
        answer.append(a[0])

    return answer