package algo0424;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class B15686_치킨배달 {
	static int N, M;
	static List<Integer[]> chicken;
	static int [][] city;
	static int min = Integer.MAX_VALUE;
	static int[] di = {1, -1, 0, 0};
	static int[] dj = {0, 0, 1, -1};
	static boolean[][] selected;
	
	// 유효성 체크 
	public static boolean invalidChk(int i, int j) {
		if (i<1 || j<1 || i>N || j>N) return false;
		return true;
	}
	
	// 치킨집 중 M개 고르기 
	public static void select(int idx, int s) {
		if (s==M) { // M개 결정 
			findDis(); // 치킨 거리 구하기 
			return;
		}
		if (idx>=chicken.size()) return;
		// 선택
		city[chicken.get(idx)[0]][chicken.get(idx)[1]] = 2;
		select(idx+1, s+1);
		city[chicken.get(idx)[0]][chicken.get(idx)[1]] = 0;
		// 선택 X
		select(idx+1, s);
	}
	
	// BFS 돌며 치킨 거리 구하기
	public static void findDis() {
		int d = 0;
		for(int i=1; i<N+1; i++) {
			for (int j=1; j<N+1; j++) {
				if (city[i][j] == 1) {
					d += BFS(i, j);
					if (d>min) return;
				}
			}
		}
		min = (min<d)?min:d;
	}
	
	public static int BFS(int start_i , int start_j) {
		int d = 0;
		selected = new boolean[N+1][N+1];
		Queue<Integer[]> que = new ArrayDeque<>();
		que.add(new Integer[] {start_i,start_j});
		selected[start_i][start_j] = true;
		while(!que.isEmpty()) {
			int now_i = que.peek()[0];
			int now_j = que.poll()[1];
			
			for (int i=0; i<4; i++) {
				int next_i = now_i + di[i];
				int next_j = now_j + dj[i];
				
				if (!invalidChk(next_i, next_j) || selected[next_i][next_j]) {
					continue;
				}
				if (city[next_i][next_j] == 2) { // 치킨집 발견 
					d = Math.abs(next_i - start_i) + Math.abs(next_j - start_j);
					return d;
				}
				que.add(new Integer[] {next_i,next_j});
				selected[next_i][next_j] = true;
			}
		}
		return d;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// 첫째줄 입력 
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		chicken = new ArrayList<Integer[]>();
		city = new int[N+1][N+1];
		// 도시 정보 입력 
		for (int i=1; i<N+1; i++) {
			st = new StringTokenizer(bf.readLine());
			for(int j=1; j<N+1; j++) {
				int n = Integer.parseInt(st.nextToken());
				if (n==1) city[i][j] = 1;
				else if (n==2) chicken.add(new Integer[] {i,j});
			}
		}
		
		select(0, 0);
		
		// 정답 출력 
		System.out.println(min);
	}

}
