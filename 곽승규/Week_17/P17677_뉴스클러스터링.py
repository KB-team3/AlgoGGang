from collections import Counter

def solution(str1, str2):
    listA = []
    listB = []
    for i in range(len(str1)-1):
        tmp = (str1[i] + str1[i+1]).upper()
        if tmp.isalpha():
            listA.append(tmp)
    for i in range(len(str2)-1):
        tmp = (str2[i] + str2[i+1]).upper()
        if tmp.isalpha():
            listB.append(tmp)
    
    Counter1 = Counter(listA)
    Counter2 = Counter(listB)
    
    inter = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())
    
    print(list(Counter1.elements()))
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        return int(len(inter) / len(union) * 65536)
    