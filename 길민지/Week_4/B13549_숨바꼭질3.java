import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class B13549_숨바꼭질3 {
	static int result;
	static int[] dx = {0, -1, 1}; // 순간이동, 걷기 
	static boolean [] visited = new boolean[100001];
	
	// 범위 체크 
	public static boolean chkValid(int x) {
		if (x<0 || x>100000) return false;
		return true;
	}
	
	public static int BFS(int n, int k) {
		Queue <Integer[]> que = new ArrayDeque<>();
		que.add(new Integer[] {n,0}); // {위치, 소요시간}
		
		while(!que.isEmpty()) {
			int now = que.peek()[0]; // 현재 위치 
			int t = que.poll()[1]; // 현재 소요시간 
			
			if (now == k) return t; // 동생 찾음!!
			
			// 이동 
			for (int i=0; i<3; i++) {
				int next = now + dx[i];
				int next_t = t + 1;
				if (i==0) { // 순간 이동 
					next = now * 2;
					next_t -= 1;
				}
				
				if (!chkValid(next)||visited[next]) continue;
				
				visited[next] = true;
				que.add(new Integer[] {next, next_t});
			}
		}
		return 0;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		// 입력 
		int n = sc.nextInt();
		int k = sc.nextInt();
		
		// 출력 
		System.out.println(BFS(n, k));
	}

}
