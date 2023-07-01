function solution(fees, records) {
    let answer = [];
    var result = {};
    let cur = {};   // 현재 주차장의 상태
    
    for (let r of records) {
        // 시각, 차량 번호, 내역 순서대로 입력
        let [time, car_num, state] = r.split(" ");
        
        // 입차 시 현재 주차장 상태에 번호와 시간 등록
        if (state === "IN") {
            cur[car_num] = time;
        } else {
            // 출차 시 result에 주차 시간 저장
            let spent = Number(time.split(":")[0] * 60) + Number(time.split(":")[1]) - (Number(cur[car_num].split(":")[0] * 60) + Number(cur[car_num].split(":")[1]));
            // 처음 주차하는 차인지, 주차한 적 있는 차인지 구분
            if (car_num in result) {
                result[car_num] += spent;
            } else {
                result[car_num] = spent;
            }
            delete cur[car_num];
            
        }
        
    }
    
    // 출차를 하지 않고 남아있는 차가 있으면 소요 시간 계산 (23:59) 기준
    if (Object.keys(cur).length > 0) {
        for (let c of Object.keys(cur)) {
            let spent = 23 * 60 + 59 - (Number(cur[c].split(":")[0] * 60) + Number(cur[c].split(":")[1])); 
            if (c in result) {
                result[c] += spent;
            } else {
                result[c] = spent;
            }
        }

    }
    
    // 차 번호 순서대로 답 출력해야함
    let keys = Object.keys(result).sort();
    
    // fees 배열을 이용해 주차요금 계산
    for (let k of keys) {
        if (result[k] <= fees[0]) {
            answer.push(fees[1]);
        } else {
            answer.push(fees[1] + Math.ceil((result[k] - fees[0]) / fees[2]) *  fees[3])
        }
    }
    

    return answer;
}
