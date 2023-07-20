def solution(survey, choices):
    # answer = ''
    # return answer
    length=len(survey)
    dic={}
    for i in range(length):
        if choices[i]==1:
            if survey[i][0] in dic.keys():
                dic[survey[i][0]]+=3
            else:
                dic[survey[i][0]]=3
        
        elif choices[i]==2:
            if survey[i][0] in dic.keys():
                dic[survey[i][0]]+=2
            else:
                dic[survey[i][0]]=2
            
        elif choices[i]==3:
            if survey[i][0] in dic.keys():
                dic[survey[i][0]]+=1
            else:
                dic[survey[i][0]]=1
        elif choices[i]==5:
            if survey[i][1] in dic.keys():
                dic[survey[i][1]]+=1
            else:
                dic[survey[i][1]]=1
        elif choices[i]==6:
            if survey[i][1] in dic.keys():
                dic[survey[i][1]]+=2
            else:
                dic[survey[i][1]]=2
        elif choices[i]==7:
            if survey[i][1] in dic.keys():
                dic[survey[i][1]]+=3
            else:
                dic[survey[i][1]]=3
    # print(dic)

    
    if "R" in dic.keys() and "T" not in dic.keys():
        answer="R"
    if "T" in dic.keys() and "R" not in dic.keys():
        answer="T"
    if "R" in dic.keys() and "T" in dic.keys():
        if dic["R"]>=dic["T"]:
            answer="R"
        elif dic["R"]<dic["T"]:
            answer="T"
    if "R" not in dic.keys() and "T" not in dic.keys():
         answer="R"

    if "C" in dic.keys() and "F" not in dic.keys():
            answer+="C"
    if "F" in dic.keys() and "C" not in dic.keys():
         answer+="F"
    if "C" in dic.keys() and "F" in dic.keys():
        if dic["C"]>=dic["F"]:
             answer+="C"
        elif dic["C"]<dic["F"]:
             answer+="F"
    if "C" not in dic.keys() and "F" not in dic.keys():
             answer+="C"
    if "J" in dic.keys() and "M" not in dic.keys():
             answer+="J"
    if "M" in dic.keys() and "J" not in dic.keys():
         answer+="M"
    if "J" in dic.keys() and "M" in dic.keys():
        if dic["J"]>=dic["M"]:
             answer+="J"
        elif dic["J"]<dic["M"]:
             answer+="M"
    if "J" not in dic.keys() and "M" not in dic.keys():
         answer+="J"
    if "A" in dic.keys() and "N" not in dic.keys():
             answer+="A"
    if "N" in dic.keys() and "A" not in dic.keys():
         answer+="N"
    if "A" in dic.keys() and "N" in dic.keys():
        if dic["A"]>=dic["N"]:
             answer+="A"
        elif dic["A"]<dic["N"]:
             answer+="N"
    if "A" not in dic.keys() and "N" not in dic.keys():
          answer+="A"
    return answer

# solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])
# print(solution(["TR", "RT", "TR"], [7, 1, 3]))
