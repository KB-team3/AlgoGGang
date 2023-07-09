package temp;
import java.util.*;
public class P72411_메뉴리뉴얼 {
    static int [] selection;
    static HashMap<String, Integer> map;
    static List<String> answer;

    static void combination(String s, int start, int r, int R){
        if(r==R){
            String str = "";
            for(int i=0; i<R; i++){
                str += s.charAt(selection[i]);
            }
            char[] StringtoChar = str.toCharArray();
            Arrays.sort(StringtoChar);
            str = new String(StringtoChar);

            if(map.containsKey(str)){
                int num = map.get(str);
                map.remove(str);
                map.put(str, num+1);
            }else{
                map.put(str,1);
            }
            return;
        }

        for(int i=start; i<s.length(); i++){
            selection[r] = i;
            combination(s,i+1,r+1,R);
        }
    }

    public List<String> solution(String[] orders, int[] course) {
        answer = new ArrayList<>();

        for(int i : course){
            selection = new int [i];
            map = new HashMap<String, Integer>();
            int max = 0;

            for(String s : orders){
                combination(s,0,0,i);
            }

            Set<String> keySet = map.keySet();
            for(String key : keySet){
                max = Math.max(max, map.get(key));
            }

            if(max >=2){
                for(String key : keySet){
                    if(map.get(key) == max){
                        answer.add(key);
                    }
                }
            }
        }
        Collections.sort(answer);
        return answer;
    }
}
