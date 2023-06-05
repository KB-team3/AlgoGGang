package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2579_계단오르기 {

    static int n;
    static int [] array;

    static int [] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        array = new int [300+1];
        dp = new int [300+1];

        for(int i=1; i<n+1; i++){
            st = new StringTokenizer(br.readLine());
            array[i] = Integer.parseInt(st.nextToken());
        }

        dp[0] = 0;
        dp[1] = array[1];
        dp[2] = array[1] + array[2];
        dp[3] = Math.max(array[1],array[2]) + array[3];

        for(int i=4; i<=n; i++){
            dp[i] = Math.max(dp[i-3]+array[i-1], dp[i-2]) + array[i];
        }

        System.out.println(dp[n]);

    }
}
