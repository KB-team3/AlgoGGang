def solution(word):
    vowels = ['', 'A', 'E', 'I', 'O', 'U']
    
    # 1부터 55555까지 1, 2, 3, 4, 5만 포함한 숫자 순서대로 저장 후 정렬
    idxs = [0] + sorted([str(x) for x in range(1, 55556) if check(str(x))])

    idx_word = ''      # 입력된 문자열을 숫자로 변경
    for w in word:
        idx_word += str(vowels.index(w))

    return idxs.index(idx_word)

def check(check_num):
    # 12345만 포함하고 있는지 체크하는 함수
    return all(n in '12345' for n in check_num)

# check 함수 이렇게 정의하면 시간은 더 빠름
# def check(n):
#     if '0' not in n and '6' not in n and '7' not in n and '8' not in n and '9' not in n:
#         return True
#     else:
#         return False
