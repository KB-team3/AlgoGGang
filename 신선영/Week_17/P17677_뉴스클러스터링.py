import math

def cut(s1, s2):    # 문자 등 불가능한 경우 제외
    if 65 <= ord(s1) <= 90 or 97 <= ord(s1) <= 122:
        if 65 <= ord(s2) <= 90 or 97 <= ord(s2) <= 122:
            return ''.join([s1.upper(), s2.upper()])
    
def solution(str1, str2):
    answer = 0
    
    set1 = []
    set2 = []
    
    for i in range(len(str1) - 1):
        c = cut(str1[i], str1[i + 1])
        if c:
            set1.append(c)
    for i in range(len(str2) - 1):
        c = cut(str2[i], str2[i + 1])
        if c:
            set2.append(c)

    union = set1.copy()
    copied = set1.copy()
    
    for s in set2:
        if s not in copied:
            union.append(s)
        else:
            copied.remove(s)

            
    inter = []
    for s in set1:
        if s in set2:
            set2.remove(s)
            inter.append(s)

    if len(union) == 0:
        return 65536
    else:
        return math.floor(len(inter) / len(union) * 65536)
