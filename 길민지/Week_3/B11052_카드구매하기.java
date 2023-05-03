import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11052_카드구매하기 {
	static int N;
	static int P[];
	static int MAX[];
	
	public static void main (String [] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// 입력 및 초기화
		N = Integer.parseInt(st.nextToken());
		P = new int [N+1];
		MAX = new int [N+1];
		
		st = new StringTokenizer(bf.readLine());
		for (int i=1; i<N+1; i++) {
			P[i] = Integer.parseInt(st.nextToken());
		}
		
		// MAX[i]는 i장 고를 때 가장 비싼 가격을 저장하는 배열
		MAX[1] = P[1];
		
		for (int i=2; i<=N; i++) { // MAX[2] ~ MAX[N] 구하기
			int max = 0;
			for (int j=1; j<=i/2; j++) { // i/2 이후부터는 중복으로 구하는거니까 안 돌아도 됨
				max = Math.max(max, MAX[j] + MAX[i-j]);
			}
			max = Math.max(max, P[i]);
			MAX[i] = max;
		}
		
		// 출력
		System.out.println(MAX[N]);
	}
}
