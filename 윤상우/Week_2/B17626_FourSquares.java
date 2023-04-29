package DP;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B17626_FourSquares {
    static int n;
    static int min;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        int [] dp = new int [n+1];

        dp[1] = 1;

        for(int i=2; i<=n; i++){
            min = Integer.MAX_VALUE;
            for(int j=1; j*j <=i; j++){
                int temp = i - j*j;
                min = Math.min(min, dp[temp]);
            }
            dp[i] = min + 1;
        }

        System.out.println(dp[n]);
    }

}