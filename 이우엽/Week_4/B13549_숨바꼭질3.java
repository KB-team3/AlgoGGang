import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B13549_숨바꼭질3 {
	static int N;
	static int K;
	static int[] dx = {-1, 1, 2};
	static List<Integer> list = new ArrayList<>();
	static int result;
	public static void permutation(int r, int cur) {
		System.out.println("r: " + r);
		System.out.println("cur: " + cur);
		if(cur < 0 || cur > 100000) {
			return;
		}
		// 종료조건
		if(cur == K) {
			list.add(r);
			return;
		}
		
		// 재귀적확장
		for(int i = 0; i < 3; i++) {
			int move = dx[i];
			int next = cur;
			// 걸을 때
			if(Math.abs(move) == 1) {
				next += move;
				result++;
			} else { // 순간이동할때
				next *= move;
			}
			permutation(r+1, next);
		}
		

		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		//start
		N = Integer.parseInt(token.nextToken());
		//dest
		K = Integer.parseInt(token.nextToken());
		//수빈이가 동생을 찾을 때까지
		
		permutation(0, N);
		
		System.out.println("list: " + list);
	}
}
