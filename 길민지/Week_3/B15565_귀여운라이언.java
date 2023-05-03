import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B15565_귀여운라이언 {
	static int N, K;
	static List<Integer> lion;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		lion = new ArrayList<>();
		
		st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (num==1) lion.add(i); // 라이언 인형인 경우 인덱스를 저장
		}
		
		if(lion.isEmpty()||lion.size()<K-1) { // 라이언이 아예 없거나, 구하려는 인형수보다 작은 경우
			System.out.println(-1);
			return;
		}
		
		int min = Integer.MAX_VALUE; // 최소 집합 개수
		for (int i=0; i<lion.size()-K+1; i++) {
			int size = lion.get(i+K-1) - lion.get(i) + 1; // 첫번째 라이언부터 돌면서 K번째 인형과의 거리차이를 구함
			min = (min<size)?min:size; // 최소값 갱신
		}
		
		// 출력
		System.out.println(min);
	}

}
