def solution(today, terms, privacies):
    answer = []
    term_dic = {}

    # 오늘 날짜 입력 설정
    today_year, today_month, today_date = map(int, today.split("."))

    # term 입력 설정
    for term in terms :
        k,m = term.split(" ")
        term_dic[k] = int(m)

    # privacies 입력 설정
    for idx, privacy in enumerate(privacies) : 
        year_month_date, kind = privacy.split(" ")
        year, month, date = map(int, year_month_date.split("."))

    # 계산 (파기는 kind별 달 수 일로 환산해서 -1)
        today = today_year * 12 * 28 + today_month * 28 + today_date
        expiration = year * 12 * 28 + month * 28 + date + term_dic[kind] * 28 - 1

        if today > expiration : 
            answer.append(idx + 1)

    return answer