from collections import Counter


def solution(str1, str2):
    
    arr1, arr2 = [], []

    # str1에 대한 문자쌍 배열
    for i in range(len(str1) - 1) : 
        if str1[i:i + 2].isalpha() : 
            arr1.append(str1[i:i + 2].upper())
    
    # str2에 대한 문자쌍 배열
    for i in range(len(str2) - 1) : 
        if str2[i:i + 2].isalpha() : 
            arr2.append(str2[i:i + 2].upper())

    # arr1과 arr2가 모두 공집합 일 경우
    if len(arr1) == 0 and len(arr2) == 0 : 
        return 65536
    
    # 배열의 모든 원소의 갯수를 세어주는 counter함수 이용
    c1 = Counter(arr1)
    c2 = Counter(arr2)

    # 문자열의 모든 문자쌍의 갯수 확인을 위해 갯수를 합친 값 'sum' 함수를 써준다. (처음 알게된 점)
    union = sum((c1 | c2).values())
    intersection = sum((c1 & c2).values())

    return int(intersection / union * 65536)
