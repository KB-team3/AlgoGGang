package algo0501;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B17626_FourSquares {
	static int N;
	static int dp[];
	
	public static void DP(int num) {
		for (int i=2; i<=num; i++){ // dp[2] ~ dp[num] 구하기 
			int root = (int)Math.sqrt(i);
			int min = Integer.MAX_VALUE;
			for(int j=root; j>0; j--) { // dp[i] 내에서 가능한 제곱들 다 뺴보기 
				int remain = i - j*j;
				min = min<dp[remain]+1 ? min : dp[remain]+1;
			}
			dp[i]=min;
		}
	}

	public static void main(String[] args) throws IOException {
		// 입력 
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(bf.readLine());
		
		// 초기화 
		dp = new int[N+1];
		dp[0] = 0;
		dp[1] = 1;
		
		// dp 배열 구하기 
		DP(N);
		
		// 출력 
		System.out.println(dp[N]);
	}

}
