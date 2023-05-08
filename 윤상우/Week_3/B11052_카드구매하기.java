package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11052_카드구매하기 {
    static int n;
    static int [] price;
    static int [] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        price = new int[n+1];

        st = new StringTokenizer(br.readLine());
        for(int i=1; i<=n; i++) price[i] = Integer.parseInt(st.nextToken());

        dp = new int [n+1];

        dp[0] = 0;
        dp[1] = price[1];

        for(int i=2; i<=n; i++){
            for(int j=1; j<i; j++){
                dp[i] = Math.max(dp[j] + dp[i-j], dp[i]);
            }
            dp[i] = Math.max(dp[i], price[i]);
        }

        System.out.println(dp[n]);

    }
}
