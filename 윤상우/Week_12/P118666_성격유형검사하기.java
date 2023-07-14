
package temp;

import java.util.HashMap;

public class P118666_성격유형검사하기 {
    static HashMap<String, Integer> map;
    static String answer;

    static void test(String s1, String s2){
        if(map.get(s1) > map.get(s2)){
            answer += s1;
        }else if(map.get(s1) < map.get(s2)){
            answer += s2;
        }else{
            answer += s1;
        }
    }

    public String solution(String[] survey, int[] choices) {
        answer = "";
        map = new HashMap<>();
        map.put("R",0);
        map.put("T",0);
        map.put("C",0);
        map.put("F",0);
        map.put("J",0);
        map.put("M",0);
        map.put("A",0);
        map.put("N",0);

        for(int i=0; i<survey.length; i++){
            String first = survey[i].substring(0,1);
            String second = survey[i].substring(1);

            switch(choices[i]){
                case 1:
                    map.put(first, map.get(first) + 3);
                    break;
                case 2:
                    map.put(first, map.get(first) + 2);
                    break;
                case 3:
                    map.put(first, map.get(first) + 1);
                    break;
                case 5:
                    map.put(second, map.get(second) + 1);
                    break;
                case 6:
                    map.put(second, map.get(second) + 2);
                    break;
                case 7 :
                    map.put(second, map.get(second) + 3);
                    break;
            }
        }

        test("R","T");
        test("C","F");
        test("J","M");
        test("A","N");

        return answer;
    }
}
