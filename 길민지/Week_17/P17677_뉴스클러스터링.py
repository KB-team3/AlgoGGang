def solution(str1, str2):
    list1 = []
    list2 = []
    
    # 집합 구하기
    for i in range(1, len(str1)):
        string = str1[i-1]+str1[i]
        if string.isalpha():
            list1.append(string.upper())
    for i in range(1, len(str2)):
        string = str2[i-1]+str2[i]
        if string.isalpha():
            list2.append(string.upper())
    
    if len(list1)==0 and len(list2)==0: 
        return 65536
    
    # 합집합 구하기 
    temp = list1.copy()
    union = list1.copy()

    for i in list2:
        if i not in temp:
            union.append(i)
        else:
            temp.remove(i)
    
    # 교집합 구하기
    intersection = []
    for i in list2:
        if i in list1:
            list1.remove(i)
            intersection.append(i)
            
    return int(len(intersection)/len(union)*65536)