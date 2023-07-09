import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B12865_평범한배낭 {
    static int N, K;
    static int[] w, v;
    static int[][] dp;

    public static void init() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        w = new int [N+1];
        v = new int[N+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(bf.readLine());
            w[i] = Integer.parseInt(st.nextToken());
            v[i] = Integer.parseInt(st.nextToken());
        }

        dp = new int[N+1][K+1];
    }

    public static void solution(){
        for(int i=1; i<N+1; i++){
            int mw = w[i];
            int mv = v[i];
//            for(int j=mw; j<K+1; j++){
//                dp[j] = Math.max(dp[j], mv + dp[j-mw]);
//            }
            for(int j=1; j<K+1; j++){
                if(mw>j) dp[i][j] = dp[i-1][j];
                else dp[i][j] = Math.max(dp[i-1][j], mv+dp[i-1][j-mw]);
            }
            System.out.println(Arrays.toString(dp[i]));
        }
    }

    public static void main(String args[]) throws IOException{
        init();
        solution();
        System.out.println(dp[N][K]);
    }
}
