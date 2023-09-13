from itertools import product

def solution(users, emoticons):
    ans = [0, 0]
    cnts = [10, 20, 30, 40]

    data = list(product(cnts, repeat = len(emoticons)))
    for d in data:
        cnt_user = 0
        cnt_money = 0
        
        for u in users:
            money = 0
            for idx, dd in enumerate(d):
                if dd >= u[0]:  # 구매 ㄱ
                    money += emoticons[idx] * ((100 -dd) / 100)
            if money >= u[1]:
                    cnt_user += 1
            else:
                cnt_money += money
        if cnt_user > ans[0] or cnt_user == ans[0] and cnt_money > ans[1]:
            ans = [cnt_user, cnt_money]
    
    return ans
