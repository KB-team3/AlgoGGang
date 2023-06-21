import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

def findNextWord(ary):
    i = len(ary) - 2
    while i >= 0 and ary[i] >= ary[i+1]: # 앞의 숫자가 더 작은 것을 i로 함
        i -= 1
    if i == -1:
        return False
    j = len(ary) - 1
    while ary[i] >= ary[j]: # ary[i] 보다 큰 ary[j]값을 찾음
        j -= 1 
    
    # 값 바꿔줌
    ary[i], ary[j] = ary[j], ary[i]
    
    resultList = ary[:i+1] # i값 앞에거 가지고옴
    tmpList = list(reversed(ary[i+1:]))
    resultList.extend(tmpList) # 뒷 부분 뒤집어서 result에 넣어줌
    
    return resultList
    
    
    
for _ in range(T):
    tmp = list(input().strip())
    result = findNextWord(tmp)
    
    if not result:
        print("".join(tmp))
    else:
        print("".join(result))
   