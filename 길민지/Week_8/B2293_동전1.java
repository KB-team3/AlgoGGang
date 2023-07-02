import java.util.Scanner;

public class B2293_동전1 {
    static int n, k;
    static int[] value;
    static int[] dp;

    public static void init(){
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();
        value = new int[n];
        dp = new int[k+1];
        for(int i=0; i<n; i++){
            value[i] = sc.nextInt();
        }
    }

    public static void solution(){
        for(int i=0; i<n; i++){
            int coin = value[i];
            if(coin>k) continue; // k보다 동전의 가치가 큰 경우 확인 X
            dp[coin]+=1;
            for(int j=coin+1; j<k+1; j++){ // dp 갱신
                dp[j]=dp[j]+dp[j-coin];
            }
        }
    }

    public static void main(String args[]){
       init();
       solution();
       System.out.println(dp[k]);
    }
}
