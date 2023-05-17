package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B13549_숨바꼭질3 {

    static int n;
    static int k;
    static int dp [];
    static boolean isVisited [];
    static int dx [] = {+1, -1, 2};

    static boolean isValid(int n){
        if(n < 0 || n >= dp.length) return false;
        return true;
    }

    static void bfs(int n){
        Queue<Integer> queue = new ArrayDeque<>();
        queue.offer(n);
        dp[n] = 0;
        if(n == k) return;
        isVisited[n] = true;

        while(!queue.isEmpty()){
            int now = queue.poll();
            if(isVisited[k]) break;

            for(int i=2; i>=0; i--){
                int next;
                if(i != 2){
                    next = now + dx[i];
                }else{
                    next = now*dx[i];
                }

                if(!isValid(next)) continue;
                if(isVisited[next]) continue;

                queue.offer(next);
                isVisited[next] = true;

                if(i != 2){
                    dp[next] = dp[now]+1;
                }else{
                    dp[next] = dp[now];
                }

            }
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        dp = new int [100001];
        isVisited = new boolean [100001];

        bfs(n);

        System.out.println(dp[k]);

    }
}
