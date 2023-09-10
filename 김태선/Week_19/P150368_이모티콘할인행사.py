data = [10, 20, 30, 40]
discount = []

# dfs(재귀)
def dfs(temp, depth) :  # temp : 현재 할인율 조합 리스트, depth : 현재까지 할인율 갯수
    # 모든 이모티콘에 대한 할인율을 설정한 경우
    if depth == len(temp) : 
        discount.append(temp[:])
        return

    for d in data : 
        temp[depth] += d
        dfs(temp, depth + 1)
        temp[depth] -= d

def solution(users, emoticons) : 
    max_user = 0
    max_price = 0

    # dfs 초기화
    dfs([0] * len(emoticons), 0)

    for d in range(len(discount)) : 
        join, price = 0, [0] * len(users)
        for e in range(len(emoticons)) : 
            for u in range(len(users)) : 
                # 사용자가 이모티콘을 구매할 수 있는 경우
                if users[u][0] <= discount[d][e] : 
                    price[u] += emoticons[e] * (100 - discount[d][e]) / 100

        for u in range(len(users)) : 
            # 판매금액이 사용자가 원하는 금액 이상인 경우
            if price[u] >= users[u][1] : 
                join += 1
                price[u] = 0

        # 현재 할인율 조합에 대한 가입자 수가 최대 가입자 수보다 크거나 같은 경우
        if join >= max_user : 
            if join == max_user : 
                max_price = max(max_price, sum(price))
            else : 
                max_price = sum(price)
            max_user = join

    return max_user, max_price