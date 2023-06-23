import java.util.*;
class Solution {
    Map<String, Integer[]> map; // key:차번호, value: [입차시, 입차분, 주차시간]
    Map<String, Integer> inMap; // key:차번호, value: 0 출차, 1 입차
    
    // 주차시간 계산
    public void countTimes(String[] records){
        map = new HashMap<>();
        inMap = new HashMap<>();
        
        for(String record : records){
            StringTokenizer st = new StringTokenizer(record);
            String time = st.nextToken();
            int h = Integer.parseInt(time.substring(0, 2));
            int m = Integer.parseInt(time.substring(3, 5));
            
            String carNum = st.nextToken();
            String inOut = st.nextToken();
            
            // 입차
            if (inOut.equals("IN")) {
                inMap.put(carNum, 1);
                // 주차 기록 있을 경우 누적
                if (map.containsKey(carNum)) map.put(carNum, new Integer[]{h, m, map.get(carNum)[2]});
                else map.put(carNum, new Integer[]{h, m, 0});
            }
            // 출차
            else {
                inMap.put(carNum, 0);
                Integer[] in = map.get(carNum);
                int parkingTime = (h - in[0]) * 60 + m - in[1];
                map.put(carNum, new Integer[]{0, 0, map.get(carNum)[2] + parkingTime});
            }
        }
        
        // 출차 기록 없는 경우
        for(String key : inMap.keySet()){
            if (inMap.get(key).equals(1)){
                Integer[] in = map.get(key);
                int parkingTime = (23 - in[0]) * 60 + 59 - in[1];
                map.put(key, new Integer[]{0, 0, in[2] + parkingTime});
            }
        }
    }
    
    // 정산
    public int[] countFees(int[] fees){
        int [] result = new int[map.size()];
        
        // 키 정렬
        List<String> keySet = new ArrayList<>(map.keySet());
        Collections.sort(keySet);
        
        for(int i=0; i<map.size(); i++){
            int parkingTime = map.get(keySet.get(i))[2];
            // 기본 요금인 경우
            if (parkingTime<=fees[0]) result[i] = fees[1];
            // 기본 요금 이상인 경우
            else result[i] = fees[1] + (int)Math.ceil((parkingTime-fees[0])*1.0/fees[2]) * fees[3];
        }
        
        return result;
    }
    
    public int[] solution(int[] fees, String[] records) {
        countTimes(records);
        return countFees(fees);
    }
}