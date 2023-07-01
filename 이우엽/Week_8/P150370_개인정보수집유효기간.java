import java.util.*;
class P150370_개인정보수집유효기간 {
    Map<String, Integer> map = new HashMap<>();
    String gToday;
    List<Integer> result = new ArrayList<>();
    
    public boolean checkValid(int year, int month, int day) {
        String[] todayBits = gToday.split("\\.");
        int tYear = Integer.parseInt(todayBits[0]);
        int tMonth = Integer.parseInt(todayBits[1]);
        int tDay = Integer.parseInt(todayBits[2]);
        if(tYear > year) return true;
        else if(tYear < year) return false;
        else { //년도가 같을 때
            if(tMonth < month) {
                return false;
            } else if(tMonth > month) {
                return true;
            } else {
                if(tDay >= day) {
                    return true;
                } else {
                    return false;
                }
            }
        }
    }
    public void calPeriod(String[] privacies) {
        int idx = 1;
        for(String privacy : privacies) {
            String[] privacyBits = privacy.split(" ");    
            String date = privacyBits[0];

            int plusPeriod = map.get(privacyBits[1]);
            
            String[] dateBits = date.split("\\.");
            int year = Integer.parseInt(dateBits[0]);
            int month = Integer.parseInt(dateBits[1]);
            int day = Integer.parseInt(dateBits[2]);
            
            if(month + plusPeriod > 12) {
                year++;
                month = month+plusPeriod - 12;
            } else {
                month += plusPeriod;
            }
            
            System.out.println(year + " " + month + " " + day);
            if(checkValid(year, month, day)) {
                result.add(idx);         
            }
            idx++;
        }
    }
    public void insertMap(String[] terms) {
        for(String term : terms) {
            String[] termBits = term.split(" ");
            String kind = termBits[0];
            String period = termBits[1];
            // System.out.println(kind + ": " + period);
            
            map.put(kind, Integer.parseInt(period));
        }
    }
    public int[] solution(String today, String[] terms, String[] privacies) {
        gToday = today;
        insertMap(terms);
        calPeriod(privacies);
        // checkValid(1,1,1);
        System.out.println(result);
        int[] answer = result.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}