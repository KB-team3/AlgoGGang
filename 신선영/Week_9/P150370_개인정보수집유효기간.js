function solution(today, terms, privacies) {
    var answer = [];
    
    // 오늘 날짜를 숫자로 변경
    let d = today.split(".")
    let cnt = Number(d[0] * 28 * 12) + Number(d[1] * 28) + Number(d[2])
    let i = 0;
    
    for (let i = 0; i < privacies.length; i++) {
        let p = privacies[i];
        const [date, type] = p.split(" ")
        for (let t of terms) {
            if (t.split(" ")[0] == type) {
                let dd = date.split(".")
                // 기준 날짜를 숫자로 바꿔서 오늘과 비교
                let spent = Number(dd[0] * 28 * 12) + Number(dd[1] * 28) + Number(dd[2])
                // 조건별 유효기간과 오늘과의 차이를 비교해서 지났으면 인덱스값 answer에 저장
                if (Math.abs(spent - cnt) >= (t.split(" ")[1] * 28)) {
                    answer.push(i + 1);
                }

            }
        }
    }
    return answer;
}
