package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B1932_정수삼각형 {

    static int n;
    static int [][] array;
    static int [][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        array = new int [n][n];
        dp = new int [n][n];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<=i; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        dp[0][0] = array[0][0];

        for(int i=1; i<n; i++){
            for(int j=0; j<=i; j++){
                if(j>0){
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + array[i][j];
                }else{
                    dp[i][j] = dp[i-1][j] + array[i][j];
                }
            }
        }

        Arrays.sort(dp[n-1]);

        System.out.println(dp[n-1][n-1]);
    }
}
