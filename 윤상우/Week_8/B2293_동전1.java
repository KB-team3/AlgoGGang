package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2293_동전1 {
    static int n;
    static int k;
    static int [] arr;
    static int [] dp;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        arr = new int [n+1];
        dp = new int [k+1];
        dp[0] = 1;
        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }
    public static void main(String[] args) throws IOException {
        init();

        for(int i=0; i<n; i++){
            for(int j=arr[i]; j<=k; j++){
                dp[j] += dp[j-arr[i]];
            }
        }

        System.out.println(dp[k]);
    }
}
