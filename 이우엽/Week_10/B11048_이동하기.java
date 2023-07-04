import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class B11048_이동하기 {
	static int N;
	static int M;
	static int[][] arr2d;
	static int[][] result;
	static int[] dx = {1, 0, 1};
	static int[] dy = {0, 1, 1};
	
	public static void print() {
		System.out.println();
		for(int i = 0; i < N; i++) {
			System.out.println(Arrays.toString(result[i]));
		}
	}
	public static void accSum(int x, int y) {
//		print();
		for(int i = 0; i < 3; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
//			System.out.println("nx: " + nx + ", ny: " + ny);
			if(result[nx][ny] == 0) {
				result[nx][ny] = result[x][y] + arr2d[nx][ny];
			} else {
				result[nx][ny] = Math.max(result[nx][ny], result[x][y] + arr2d[nx][ny]);
			}
			
			accSum(nx, ny);
		}
	}
	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(token.nextToken());
		M = Integer.parseInt(token.nextToken());
		
		arr2d = new int[N][M];
		result = new int[N][M];
		for(int i = 0; i < N; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < M; j++) {
				arr2d[i][j] = Integer.parseInt(token.nextToken());
			}
		}
	}
	public static void main(String[] args) throws IOException {
		init();
//		for(int i = 0; i < N; i++) {
//			System.out.println(Arrays.toString(arr2d[i]));
//		}
		result[0][0] = arr2d[0][0];
		accSum(0,0);
//		print();
		System.out.println(result[N-1][M-1]);
	}
}
