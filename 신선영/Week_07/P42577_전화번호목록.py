def solution(phone_book):
    answer = True

    # 시작하는 숫자와 길이 두 가지 기준으로 정렬
    phone_book = sorted(phone_book, key= lambda x: (len, x))


    for i in range(len(phone_book) - 1):
        if answer == False:
            break
        else: 
            txt = phone_book[i]
            l = len(txt)
            # 정렬이 완료된 상태이기 때문에 바로 뒤의 값만 확인해도 됨
            if phone_book[i + 1][:l] == txt:
                answer = False

    return answer
