def solution(phone_book):
    answer = True
    phone_book.sort()
    # return answer

    # for i in range(len(phone_book)-1):
    #     for j in range(i+1, len(phone_book)):
    #         if phone_book[i] in phone_book[j] or phone_book[j] in phone_book[i]:
    #             answer=False
    
    for i in range(len(phone_book)-1):
        if len(phone_book[i])<=len(phone_book[i+1]):
            if phone_book[i] in phone_book[i+1]:
                if phone_book[i+1][:len(phone_book[i])]==phone_book[i]:
                   answer=False
        
    return answer