def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    #print(phone_book)

    for a, b in zip(phone_book, phone_book[1:]):
        if b.startswith(a):
            answer = False
    return answer
