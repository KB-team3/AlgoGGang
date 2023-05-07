import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

public class B1941_소문난칠공주 {
	static char seat[][];
	static int N = 5;
	//static boolean checked[];
	static List<Integer> selected; // 고른 7개 자리 
	static List<Integer> S; // 이다솜파 
	static int[] di = {1, -1, 0, 0};
	static int[] dj = {0, 0, 1, -1};
	static int result;
	static int t;
	
	// 7개 자리 고르기 
	public static void select(int num, int cnt) {
		if (cnt == 7) { 
			result+=BFS(); // 연결되어 있는지 확인 
			return;
		}
		
		for (int i=num+1; i<N*N; i++) {
			selected.add(i);
			select(i, cnt+1);
			selected.remove(selected.size()-1);
		}
	}
	
	public static boolean chkValid(int i, int j) {
		if (i<0 || j<0 || i>=N || j>=N) return false;
		return true;
	}
	
	public static int BFS() {
		boolean [][] checked = new boolean[N][N];
		Queue <Integer[]> que = new ArrayDeque<>();
		
		int start = selected.get(0);
		checked[start/N][start%N] = true;
		if (S.contains(start)) que.add(new Integer[] {start, 1, 0}); // 위치, 이다솜파, 임지연파
		else que.add(new Integer[] {start, 0, 1});
		
		while(!que.isEmpty()) {
			int now = que.peek()[0];
			int s = que.peek()[1];
			int y = que.poll()[2];
			
			if (y>=4) continue; // 임지연파 4명 이상 
			if(s+y==7) {
				System.out.println(selected);
				return 1; // 7명 찾음  
			}
			
			// 4방 탐색 
			for (int i=0; i<4; i++) {
				int next_i = now/N + di[i];
				int next_j = now%N + dj[i];
				
				if (!chkValid(next_i, next_j) || checked[next_i][next_j]) continue;
				int next = next_i*N + next_j;
				
				for (int n : selected) {
					if (n == next) {
						checked[next_i][next_j] = true;
						if (S.contains(next)) que.add(new Integer[] {next, s+1, y}); 
						else que.add(new Integer[] {next, s, y+1});
					}
				}
			}
		}
		return 0;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		// 입력 및 초기화 
		seat = new char[N][N]; 
		selected = new ArrayList<>();
		S = new ArrayList<>();
		for (int i=0; i<N; i++) {
			String line = bf.readLine();
			for (int j=0; j<N; j++) {
				seat[i][j] = line.charAt(j);
				if (seat[i][j] == 'S') S.add(i*N + j);
			}
		}
		System.out.println(S);
		
		for (int i=0; i<N*N; i++) {
			selected.add(i);
			select(i, 1);
			selected.remove(selected.size()-1);
		}
		
		System.out.println(result);
	}

}
