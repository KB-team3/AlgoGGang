def solution(fees, records):
    cars={}
    # 나간 시간이 없는 경우 탐색 후 OUT을 추가
    for i in range(len(records)):
        if records[i].split(" ")[1] in cars:
            cars[records[i].split(" ")[1]]=int(cars[records[i].split(" ")[1]])+1
        else:
            cars[records[i].split(" ")[1]]=1
    for i in cars.keys():
        for j in  range(len(records)):
            if records[j].split(" ")[0]=="23:59":
                records.remove(records[j])
            elif int(i)!=2:
                records.append("23:59 "+i+" OUT")
    
    cars_times={}
    # 차 시간 구하기
    for i in cars.keys():
        cars_times[i]=[]
    
    for i in range(len(records)):
        if records[i].split(" ")[1] in cars.keys():
            cars_times[records[i].split(" ")[1]].append(records[i].split(" ")[0])
    # 차 번호 순으로 정렬
    cars_time=dict(sorted(cars_times.items()))

    # 요금 매기기
    cars_money={}
    # 차 시간 구하기
    for i in cars.keys():
        cars_money[i]=[]

    for i in cars_time.keys():
        time=int(cars_time[i][1].split(":")[0]+cars_time[i][1].split(":")[1])-int(cars_time[i][0].split(":")[0]+cars_time[i][0].split(":")[1])
        hour=time//100
        minute=time%100
        if hour*60+minute<=fees[0]:
            cars_money[i]=fees[1]
        else:
            cars_money[i]=fees[1]+(((hour-fees[0//60])*60+minute))//fees[2]*fees[3]

    return list(cars_money.values())
