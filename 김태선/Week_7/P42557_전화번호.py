def solution(phoneBook) :

    #전화번호부 사전식으로 정렬(rs: 비슷한 접두사를 가진 번호들 인접)
    phoneBook = sorted(phoneBook)

    #zip함수로 번호들을 순서쌍으로 묶기(처음 알게됨)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        #startswith함수로 주어진 접두사로 시작하는지 여부 판단(처음 알게됨)
        #즉, p2가 p1으로 시작하는지를 의미
        if p2.startswith(p1):
            return False
    return True