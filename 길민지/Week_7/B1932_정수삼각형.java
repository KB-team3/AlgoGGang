import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class B1932_정수삼각형 {
    static int N;
    static List<Integer>[] trg;

    public static void main(String args[]) throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        trg = new List[N];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            trg[i] = new ArrayList<>();
            if(i==0){ // 1층 입력
                trg[i].add(Integer.parseInt(st.nextToken()));
                continue;
            }
            for(int j=0;j<i+1; j++){
                int num = Integer.parseInt(st.nextToken()); // 현재 위치의 수
                int prev; // 이전 층의 수
                if (j==0) prev=trg[i-1].get(j);
                else if(j==i) prev=trg[i-1].get(j-1);
                else prev=Math.max(trg[i-1].get(j), trg[i-1].get(j-1));
                trg[i].add(prev+num);
            }
        }

        // 마지막층 최대값 출력
        System.out.println(Collections.max(trg[N-1]));
    }
}
