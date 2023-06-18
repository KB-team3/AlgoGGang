import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2293_동전1 {
	static int n;
	static int k;
	static int[] coins;
	static int cnt;
	public static void dp(int x) {
		//구글링 해봤는데
//		0 1 2 3 4 5 6 7 8 9 10
//		----------------------
//		1 1 1 1 1 1 1 1 1 1 1  (1만이용)
//		0 0 1 1 2 2 3 3 4 4 5  (1,2이용)
//		0 0 0 0 0 1 1 2 2 3 4  (1,2,5이용)
		//여기까진 이해했는데,
		//여기에 대한 점화식이 왜 dp[i] = dp[i] + dp[i-coin]; 이렇게 나오는지 모르겠다
	}
	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		n = Integer.parseInt(token.nextToken());
		k = Integer.parseInt(token.nextToken());
		coins = new int[n];
		
		for(int i = 0; i < n; i++) {
			coins[i] = Integer.parseInt(br.readLine());
		}
	}
	public static void main(String[] args) throws IOException {
		init();
		System.out.println(Arrays.toString(coins));
		dp(10);

	}
}
