import java.util.*;
class CarInfo implements Comparable<CarInfo>{
    int carNum;
    int hour;
    int minutes;
    String message;
    int fee;
    CarInfo(int carNum, int hour, int minutes, String message) {
        this.carNum = carNum;
        this.hour = hour;
        this.minutes = minutes;
        this.message = message;
    }
    public String toString() {
        return hour + " " + minutes + " " + message;
    }
    public int compareTo(CarInfo o) {
        return this.carNum - o.carNum;
    }
}
class Solution {
    int BASIC_TIME;
    int BASIC_FEE;
    int UNIT_TIME;
    int UNIT_FEE;
    Map<String, CarInfo> map = new HashMap<>();
    Map<String, Integer> minMap = new HashMap<>();
    
    public void recal(String key) {
        CarInfo info = map.get(key);
        int hour = info.hour;
        int min = info.minutes;
        
        hour = 23 - hour;
        min = 59 - min;
        int transMin = (hour * 60) + min;
        if(minMap.containsKey(key)) {
            transMin += minMap.get(key);  
        }
        minMap.put(key, transMin);
    }
    public int calFee(int accMin) {
        ///////////////////요금cal
        int fee = 0;
        if(accMin <= BASIC_TIME) {
            fee += BASIC_FEE;
        } else { //기본시간 초과
            fee = BASIC_FEE + (int)Math.ceil((accMin-BASIC_TIME)/(double)UNIT_TIME) * UNIT_FEE;
        }
        System.out.println("fee: " + fee);
        return fee;
    }
    public void cal(String carNum, CarInfo prev, CarInfo cur) {
        // System.out.println("prev: " + prev);
        // System.out.println("cur: " + cur);
        ///////////////////시간cal
        int min = cur.minutes - prev.minutes; 
        if(min < 0) {
            min = cur.minutes + (60-prev.minutes);
            cur.hour = cur.hour-1;
        }
        int hour = cur.hour - prev.hour;
        // System.out.println("hour: " + hour + " min: " + min);
        int transMin = hour * 60 + min;
        if(minMap.containsKey(carNum)) {
            minMap.put(carNum, minMap.get(carNum)+transMin);
        } else {
            minMap.put(carNum, transMin);    
        }
    }
    public void insert(String record) {
        String[] recordBits = record.split(" ");
        String time = recordBits[0];
        String[] timeBits = time.split(":");
        int hour = Integer.parseInt(timeBits[0]);
        int minutes = Integer.parseInt(timeBits[1]);
        String carNum = recordBits[1];
        String message = recordBits[2];
        // System.out.println(hour + " " + minutes);
        CarInfo info = new CarInfo(Integer.parseInt(carNum), hour, minutes, message);
        if(message.equals("OUT") && map.containsKey(carNum)) {
            cal(carNum, map.get(carNum), info);
            map.get(carNum).message = "OUT";
        } else {
            map.put(carNum, info);    
        }
    }
    public int[] solution(int[] fees, String[] records) {
        
        BASIC_TIME = fees[0];
        BASIC_FEE = fees[1];
        UNIT_TIME = fees[2];
        UNIT_FEE = fees[3];
        for(String record : records) {
            insert(record);            
        }
        
        for(String key : map.keySet()) {
            if(map.get(key).message.equals("IN")) {
                recal(key);
            }
        }
        CarInfo[] result = new CarInfo[minMap.size()];
        int i = 0;
        for(String key : minMap.keySet()) {
            int accMin = minMap.get(key);
            int fee = calFee(accMin);
            map.get(key).fee = fee;
            result[i] = map.get(key);
            i++;
        }
        
        Arrays.sort(result);
    
        int[] answer = new int[result.length];
        for(int t = 0; t < result.length; t++) {
            answer[t] = result[t].fee;
        }
        
        return answer;
    }
}