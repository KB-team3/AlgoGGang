import java.util.*;
class Solution {
    
    public static Map<String, Integer>[] mapArr;
    public static int N;
    public static List<String> list;

    public static void sol(String[] orders, int[] course){

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
    
    public static void combination(String order, int i, int n, int r, char[] c, Map<String, Integer> map){ 
        // 코스, 배열 인덱스, 위치, 배열 크기, 배열
        if(i==r){
            char[] newArr = c.clone();
            Arrays.sort(newArr);
            String s = new String(newArr);
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
    
    public String[] solution(String[] orders, int[] course) {
        mapArr = new Map[course.length];
        list = new ArrayList<>();
        sol(orders, course);
        
        System.out.println(list);
        
        String[] answer = list.stream()
                            .toArray(String[]::new);
        return answer;
    }
}



