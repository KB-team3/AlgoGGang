import java.util.*;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        List<Integer> list = new ArrayList<>();
        Integer[] answer = {};
        
        // 오늘 날짜 parsing
        int ty = Integer.parseInt(today.substring(0,4));
        int tm = Integer.parseInt(today.substring(5,7));
        int td = Integer.parseInt(today.substring(8,10));
        
        // privacies 확인
        for(int i=0; i<privacies.length; i++){
            StringTokenizer st = new StringTokenizer(privacies[i]);
            String pday = st.nextToken();
            String ptype = st.nextToken();
            int pterm = 0;
            
            // 약관 유효기간 찾기
            for(String term : terms){
                StringTokenizer st2 = new StringTokenizer(term);
                String type = st2.nextToken();
                if (type.equals(ptype)) pterm = Integer.parseInt(st2.nextToken());
            }
            
            // 개인정보 수집 일자
            int py = Integer.parseInt(pday.substring(0,4));
            int pm = Integer.parseInt(pday.substring(5,7));
            int pd = Integer.parseInt(pday.substring(8,10));
            
            // 만료일자로 변경
            pm += pterm;
            py += (pm-1)/12;
            pm %= 12;
            if(pm==0) pm=12;
            
            // 오늘 날짜랑 비교
            if (py<ty) {
                list.add(i+1);
            } else if (py==ty) {
                if (pm<tm){
                    list.add(i+1);
                } else if (pm==tm) {
                    if (pd<=td) list.add(i+1);
                }
            }
        }
        // 배열로 변환
        return list.stream().mapToInt(i -> i).toArray();
    }
}