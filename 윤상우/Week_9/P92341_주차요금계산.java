package temp;

import java.util.*;

public class P92341_주차요금계산 {
    public int[] solution(int[] fees, String[] records) {
        HashMap<Integer, Integer> map = new HashMap<>();
        HashMap<Integer, Integer> map_cal = new HashMap<>();
        List<Integer> list = new ArrayList<>();

        for(String r : records){
            int num = Integer.parseInt(r.substring(6,10));
            if(!map.containsKey(num)){
                map.put(num,0);
                list.add(num);
            }
        }

        for(String r : records){
            int hour = Integer.parseInt(r.substring(0,2));
            int minute = Integer.parseInt(r.substring(3,5));
            int num = Integer.parseInt(r.substring(6,10));
            String record = r.substring(11);

            int time = hour * 60 + minute;

            if(record.equals("IN")){
                map_cal.put(num, time);
            }else{
                int temp = map_cal.get(num);
                map_cal.remove(num);
                map.put(num, map.get(num) + time - temp);
            }
        }

        list.sort((o1,o2) -> o1 - o2);

        int[] answer = new int [list.size()];

        for(int i : list){
            if(map_cal.containsKey(i)){
                map.put(i, map.get(i) + 1439 - map_cal.get(i));
            }
        }

        for(int i=0; i<list.size(); i++){
            int money = 0;
            int time = map.get(list.get(i));
            if(time > fees[0]){
                if((time - fees[0]) % fees[2] > 0){
                    money += fees[1] + ((time - fees[0]) / fees[2] + 1)  * fees[3];
                }else{
                    money += fees[1] + ((time - fees[0]) / fees[2]) * fees[3];
                }
            }else{
                money += fees[1];
            }

            answer[i] = money;

        }

        System.out.println(map);

        return answer;
    }
}