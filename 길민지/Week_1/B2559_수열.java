import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2559_수열 {
	static int N, K;
	static int temp[];
	static int maxTemp = -Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// 첫째줄 입력 
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		// 둘째줄 입력 
		temp = new int[N+1];
		temp[0] = 0;
		st = new StringTokenizer(bf.readLine());
		for (int i=1; i<N+1; i++) {
			temp[i] = temp[i-1] + Integer.parseInt(st.nextToken()); // 누적합 저장 
		}
		
		// K일의 온도의 합 구하기 
		for(int i=0; i<N+1-K; i++) {
			int tempK = temp[i+K] - temp[i];
			maxTemp = (maxTemp>tempK)?maxTemp:tempK;
		}
		
		// 최댓값 출력 
		System.out.print(maxTemp);
	}

}
