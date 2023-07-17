package temp;
import java.util.*;

public class P155651_호텔대실 {
    public int solution(String[][] book_time) {
        int answer = 1;
        int len = book_time.length;
        int [][] book_int = new int [len][2];

        for(int i=0; i<len; i++){
            int start = Integer.parseInt(book_time[i][0].substring(0,2)) * 60 + Integer.parseInt(book_time[i][0].substring(3));
            int end = Integer.parseInt(book_time[i][1].substring(0,2)) * 60 + Integer.parseInt(book_time[i][1].substring(3));

            book_int[i] = new int []{start,end};
        }

        Arrays.sort(book_int, (o1,o2) -> (o1[0] - o2[0]));

        for(int i=0; i<len; i++){
            System.out.println(book_int[i][0] + ", " + book_int[i][1]);
        }

        PriorityQueue<Integer> que = new PriorityQueue<>();
        que.add(book_int[0][1]+10);

        for(int i=1; i<len; i++){
            int in = book_int[i][0];
            int out = que.poll();

            if(out > in){
                answer++;
                que.add(out);
                que.add(book_int[i][1] + 10);
            }else{
                que.add(book_int[i][1] + 10);
            }
        }

        return answer;
    }
}
