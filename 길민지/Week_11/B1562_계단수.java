import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class B1562_계단수 {
    static int N;
    static int dp[][][];
    static final int MOD = 1000000000;
    static int result;
    public static void init(){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        dp = new int [10][N][1<<10];
        for(int i=0; i<10; i++){
            dp[0][i][1<<i] = 1;
        }
    }

    public static void solution(){
        for(int i=1; i<N; i++){ // 길이가 i인 숫자까지
            for(int j=0; j<10; j++){ // 0~9 넣기
                for (int k=0; k<(1<<10); k++){
                    if(j>0){ // -1 기록 추가
                        dp[i][j][k|(1<<j)] += dp[i-1][j-1][k] % MOD;
                    }
                    if(j<9){ // +1 기록 추가
                        dp[i][j][k|(1<<j)] += dp[i-1][j+1][k] % MOD;
                    }
                    dp[i][j][k|(1<<j)] %= MOD;
                }
            }
        }

        for(int i=0; i<10; i++){
            result += dp[N-1][i][1023]%MOD; // 이진수 1111111111의 개수 (0~9까지 다 방문한 경우)
            result %= MOD;
        }
    }
    public static void main(String args[]){
        init();
        solution();
        System.out.println(result);
    }
}
