import math

def solution(fees, records):
    parking = dict()
    stack = dict()

    for record in records : 
        time, num, state = record. split(" ")
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)

        if state == "IN" : 
            parking[num] = minutes
        
        # 출차 기록이 없는 차량 (keyError 발생 시 예외처리)
        elif state == "OUT" : 
            try : 
                stack[num] += minutes - parking[num]
            except : 
                stack[num] = minutes - parking[num]
            
            # 출차 차량 삭제
            del parking[num]
    
    # 출차 기록 없는 차 23:59 출차 처리
    for num, minute in parking.items() : 
        try : 
            stack[num] += 23 * 60 + 59 - minute
        except : 
            stack[num] = 23 * 60 + 59 - minute


    result = []

    # 문제에서 제공한 요금계산 방법으로 요금계산 함수 정의
    def get_fee(minutes, fees):
        return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

    # stack dict 항목 lambda로 num 기준으로 오름차순 정렬
    for num, time in sorted(stack.items(), key = lambda x : x[0]) :
        fee = get_fee(time, fees)
        result.append(fee)

    return result
