import math


# 주차요금계산
def calcFee(time, baseTime, baseFee, unitT, unitF):
    resultFee = 0
    plusTime = max(0, time - baseTime)  # time이 기본시간 초과했으면 몇분 초과했는지 결과를 저장
    plusFee = math.ceil(plusTime / unitT) * unitF
    resultFee = baseFee + plusFee

    return resultFee


def solution(fees, records):
    answer = []
    parking = {}  # 주차장에 들어오는 것들 기록
    parkResult = {}

    # 요금 정보 분리
    baseTime = fees[0]
    baseFee = fees[1]
    unitT = fees[2]
    unitF = fees[3]

    for r in records:
        time, number, state = r.split()
        h, m = time.split(":")
        time = int(h) * 60 + int(m)  # 시간을 분으로 바꿈!

        if state == "IN":
            parking[number] = time
        else:
            if number in parkResult:
                parkResult[number] += time - parking[number]
            else:
                parkResult[number] = time - parking[number]

            del parking[number]  # 기록 지우기

    # 아직 출차 안한 차 요금계산
    for carNum in parking:
        if carNum in parkResult:
            parkResult[carNum] += (23 * 60 + 59) - parking[carNum]  # 23:59이 출차시간으로 간주
        else:
            parkResult[carNum] = (23 * 60 + 59) - parking[carNum]  # 23:59이 출차시간으로 간주

    for carNum in parkResult:
        fee = calcFee(parkResult[carNum], baseTime, baseFee, unitT, unitF)
        answer.append([carNum, fee])

    answer.sort()
    answer = [a[1] for a in answer]

    return answer
