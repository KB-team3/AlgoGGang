import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class B15686_치킨배달 {
	static int[][] arr2d;
	static boolean[][] isVisited;
	static int[] dx = {-1, 0, 1, 0};
	static int[] dy = {0, 1, 0, -1};
	static int N;
	static int M;
	static int dist;
	static List<Integer> list = new ArrayList<>();
	static boolean checkValid = true;
	public static void bfs(int i, int j) {
		Queue<int[]> queue = new ArrayDeque<>();
		isVisited[i][j] = true;
		// 처음 좌표가 치킨집일때
		if(arr2d[i][j] == 2) {
			return;
		}
		queue.offer(new int[] {i, j});
		while(!queue.isEmpty()) {
			int[] node = queue.remove();
			int x = node[0];
			int y = node[1];
			System.out.print("x: " + x);
			System.out.println(" y: " + y);
			for(int t = 0; t < 4; t++) {
				int nx = x + dx[t];
				int ny = y + dy[t];
				if(nx <= 0 || nx > N || ny <= 0 || ny > M) {
					continue;
				}
				// 치킨집에 도착햇을 때, 초기화
				if(arr2d[nx][ny] == 2) {
					checkValid = false;
					// 초기화
					break;
				}
				// 다음 좌표가 빈칸이고 방문하지 않았다면	
				if(arr2d[nx][ny] == 0 && !isVisited[nx][ny]) {
					System.out.print("nx: " + nx);
					System.out.println(" ny: " + ny);
					isVisited[nx][ny] = true;
					queue.offer(new int[] {nx, ny});
				}
			}
			dist++;
			if(!checkValid) {
				System.out.println("dist: " + dist);
				list.add(dist);
				break;
			}
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(token.nextToken());
		M = Integer.parseInt(token.nextToken());
		arr2d = new int[N+1][N+1];
		isVisited = new boolean[N+1][N+1];
		
		for(int i = 1; i < N+1; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			for(int j = 1; j < N+1; j++) {
				arr2d[i][j]= Integer.parseInt(token.nextToken());
			}
		}
		
		// test 출력
		for(int i = 1; i < N+1; i++) {
			for(int j = 1; j < N+1; j++) {
				System.out.print(arr2d[i][j] + " ");
			}
			System.out.println();
		}
		
		for(int i = 1; i < N+1; i++) {
			for(int j = 1; j < N+1; j++) {
				// 현재 위치가 집이면
				if(arr2d[i][j] == 1) {
					isVisited= new boolean[N+1][N+1];
					dist = 0;
					checkValid = true;
					bfs(i, j);
				}
			}
		}
		System.out.println(list);
	}
}
