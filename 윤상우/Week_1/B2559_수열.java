package 누적합;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2559_수열 {

    static int n;
    static int k;
    static int [] dp;
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        dp = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            dp[i+1] = dp[i] + Integer.parseInt(st.nextToken());
        }

        ans = Integer.MIN_VALUE;
        for(int i=0; i<=n-k; i++){
            int temp = dp[i+k] - dp[i];
            ans = Integer.max(ans, temp);
        }

        System.out.println(ans);
    }
}
