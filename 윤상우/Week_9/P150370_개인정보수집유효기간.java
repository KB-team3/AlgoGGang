package temp;

import java.time.LocalDate;
import java.util.*;

public class P150370_개인정보수집유효기간 {

    public static int [] solution(String today, String[] terms, String[] privacies) {
        List<Integer> list = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        String [] todayDate = today.split("\\.");


        for(String t : terms){
            String type = t.substring(0,1);
            int month = Integer.parseInt(t.substring(2));
            map.put(type, month);
        }

        int len = privacies.length;

        for(int i=0; i<len; i++){
            String date = privacies[i].substring(0, privacies[i].length()-2);
            String type = privacies[i].substring(privacies[i].length()-1);

            int term = map.get(type);

            String [] arr = date.split("\\.");

            int year = term/12;
            int mon = term%12;

            int yearEff = Integer.parseInt(arr[0]) + year;
            int monthEff = Integer.parseInt(arr[1]) + mon;
            int dayEff = Integer.parseInt(arr[2]);

            if(monthEff > 12){
                yearEff += 1;
                monthEff -= 12;
            }

            if(yearEff < Integer.parseInt(todayDate[0])){
                list.add(i+1);
            }else if (yearEff == Integer.parseInt(todayDate[0])){
                if(monthEff < Integer.parseInt(todayDate[1])){
                    list.add(i+1);
                } else if (monthEff == Integer.parseInt(todayDate[1])){
                    if(dayEff <= Integer.parseInt(todayDate[2])){
                        list.add(i+1);
                    }else{
                        continue;
                    }
                } else {
                    continue;
                }
            }else{
                continue;
            }

        }

        int [] answer = new int [list.size()];
        for(int i=0; i<answer.length; i++){
            answer[i] = list.get(i);
        }

        return answer;
    }

    public static void main(String[] args) {
        solution("2022.05.19", new String[]{"A 6", "B 12", "C 3"}, new String[]{"2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"});
    }
}
