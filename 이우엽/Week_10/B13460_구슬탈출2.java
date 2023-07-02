import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class B13460_구슬탈출2 {
	static int N;
	static int M;
	static char[][] arr2d;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int flag = 1;
	
	public static void print() {
		for(int i = 0; i < N; i++) {
			System.out.println(Arrays.toString(arr2d[i]));
		}
	}
	public static void implement(int[] locR, int[] locB, int[] target) {
		int xr = locR[0];
		int yr = locR[1];
		
		int xb = locB[0];
		int yb = locB[1];
		boolean[][] isVisited = new boolean[N][M];
		Queue<int[]> queue = new ArrayDeque<>();
		isVisited[xr][yr] = true;
		queue.offer(new int[]{xr, yr});
		while(!queue.isEmpty()) {
			int[] cur = queue.remove();
			
			for(int i = 0; i < 1; i++) {
				int nx = cur[0] + dx[i];
				int ny = cur[1] + dy[i];
				
				int nx_b = xb + dx[i];
				int ny_b = yb + dy[i];
				
				if(arr2d[nx][ny] == '#') continue;
				while(arr2d[nx][ny] == '.' && !isVisited[nx][ny]) {
					if(arr2d[nx_b][ny_b] == 'O') {
						flag = 0;
						return;
					}
					
					if(arr2d[nx][ny] == 'O') {
						break;
					}
					isVisited[nx][ny] = true;
					queue.offer(new int[]{nx, ny});
					
					nx = cur[0] + dx[i];
					ny = cur[1] + dy[i];
					
					if(arr2d[nx_b][ny_b] != '#') {
						nx_b = nx_b + dx[i];
						ny_b = ny_b + dy[i];
					}
				}
				arr2d[nx][ny] = 'R';
			}
			print();
			System.out.println();
		}
	}
	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(token.nextToken());
		M = Integer.parseInt(token.nextToken());
		
		arr2d = new char[N][M];
		for(int i = 0; i < N; i++) {
			String arr = br.readLine();
			arr2d[i] = arr.toCharArray();
		}
	}
	public static void main(String[] args) throws IOException {
		init();
		
		//R, B, O 위치 찾기
		int[] locR = new int[2];
		int[] locB = new int[2];
		int[] locO = new int[2];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(arr2d[i][j] == 'R') {
					locR[0] = i;
					locR[1] = j;
				} else if(arr2d[i][j] == 'B') {
					locB[0] = i;
					locB[1] = j;
				} else if(arr2d[i][j] == 'O') {
					locO[0] = i;
					locO[1] = j;
				}
			}
		}
		
		System.out.println("R:" + locR[0] + " " + locR[1]);
		System.out.println("B:" + locB[0] + " " + locB[1]);
		implement(locR, locB, locO);
	}
}
