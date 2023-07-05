package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11048_이동하기 {
    static int n;
    static int m;
    static int [][] array;
    static int [][] dp;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        array = new int [n+1][m+1];
        dp = new int[n+1][m+1];

        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<=m; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void main(String[] args) throws IOException {
        init();

        for(int i=1; i<=n; i++){
            for(int j=1; j<=m; j++){
                if(i==1 && j!=1){
                    dp[i][j] = dp[i][j-1] + array[i][j];
                }else if(j==1 && i!=1){
                    dp[i][j] = dp[i-1][j] + array[i][j];
                }else if(i==1 && j==1){
                    dp[i][j] = array[i][j];
                }
                else{
                    dp[i][j] = Math.max(dp[i-1][j-1],Math.max(dp[i-1][j],dp[i][j-1])) + array[i][j];
                }
            }
        }

        System.out.println(dp[n][m]);

    }
}
