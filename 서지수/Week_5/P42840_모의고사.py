def solution(answers):
    result=[]
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    one_result=0;
    two_result=0;
    three_result=0;
    
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            one_result+=1; # 맞춘 개수
        if answers[i]==two[i%8]:
            two_result+=1
        if answers[i]==three[i%10]:
            three_result+=1
        
    result=[one_result,two_result,three_result]
   
    if max(result)==one_result==two_result==three_result:
        return [1,2,3]
    if max(result)==one_result==two_result:
        return [1,2]
    if max(result)==one_result==three_result:
        return [1,3]   
    if max(result)==two_result==three_result:
        return [2,3]
    if max(result)==one_result:
        return [1]
    if max(result)==two_result:
        return [2]
    if max(result)==three_result:
        return [3]