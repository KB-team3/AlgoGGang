import java.util.*;

public class P72411_메뉴리뉴얼 {
    public static Map<String, Integer>[] mapArr;
    public static int N;
    public static List<String> list;

    public static void solution(String[] orders, int[] course){

            for(int i=0; i<course.length; i++){
                int r = course[i];
                mapArr[i] = new HashMap<>();
                for(String order : orders){
                //nCr 구하기
                char[] c = new char[r];
                combination(order, 0,0, r, c, mapArr[i]);
                }
            }

        for(int i=0; i<course.length; i++){
            int max = 2;
            for(String key : mapArr[i].keySet()){
                max = Math.max(max, mapArr[i].get(key));
            }
            for(String key : mapArr[i].keySet()){
                if(mapArr[i].get(key)==max) list.add(key);
            }
        }
        Collections.sort(list);
    }
    public static void combination(String order, int i, int n, int r, char[] c, Map<String, Integer> map){ // 코스, 배열 인덱스, 위치, 배열 크기, 배열
        if(i==r){
            Arrays.sort(c);
            String s = new String(c);
            System.out.println(s);
            if(map.containsKey(s)){
                map.put(s, map.get(s)+1);
            }
            else{
                map.put(s, 1);
            }
            return;
        }
        if(n>=order.length()) return;
        // 선택x
        combination(order, i, n+1, r, c, map);
        // 선택o
        c[i] = order.charAt(n);
        combination(order, i+1, n+1, r, c, map);
    }

    public static void main(String args[]){
        String orders [] = {"XYZ", "XWY", "WXA"};
        int course [] = {2,3,4};
        mapArr = new Map[course.length];
        list = new ArrayList<>();
        solution(orders, course);
        String[] answer = list.stream()
                .toArray(String[]::new);

        System.out.println(Arrays.toString(answer));
    }
}
