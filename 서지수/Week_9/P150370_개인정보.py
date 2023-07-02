def solution(today, terms, privacies):
    days=[]
    result = []
    for i in range(len(privacies)):
        for j in range(len(terms)):
            if privacies[i].split(" ")[1]==terms[j].split(" ")[0]:
                date=privacies[i].split(" ")[0].split(".")
                # day하루 빼기
                if int(date[2])-1==0:
                    date[2]=28
                    date[1]=int(date[1])-1
                else:
                    date[2]=int(date[2])-1
                # 달 더해주기
                if int(date[1])+int(terms[j].split(" ")[1])>12:
                    date[1]=int(date[1])+int(terms[j].split(" ")[1])-12
                    date[0]=int(date[0])+1
                else:
                    date[1]=int(date[1])+int(terms[j].split(" ")[1])
                days.append(date)
                # print(days)

    # 파쇄해야하는 날짜 append
    for k in range(len(days)):
        if int(days[k][0])<int(today.split(".")[0]):
            result.append(k+1)
        elif int(days[k][1])<int(today.split(".")[1]):
            result.append(k+1)
        elif int(days[k][2]) <int(today.split(".")[2]):
            result.append(k+1)
            
    result.sort()
    return result
