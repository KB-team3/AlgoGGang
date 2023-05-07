import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B1941_소문난칠공주 {
	static char[][] arr2d = new char[5][5];
	static boolean[][] isVisited = new boolean[5][5];
	static int[] dx = {0, 1, 0, -1};
	static int[] dy = {1, 0, -1, 0};
	static int cnt = 1;
	static int sCnt = 0;
	static int result;
	static List<int[]> list = new ArrayList<>();
	public static void DFS(int x, int y, int r) {
		if(r == 7) {
			if(sCnt >= 4) {
				for(int i = 0; i < list.size(); i++) {
					int[] aa = list.get(i);
					System.out.println("x: " + aa[0] + ", y: " + aa[1]);
				}
				System.out.println("------------");
				result++;
			}
			return;
		}
		
		// 이다솜파일때, sCnt++;
		if(arr2d[x][y] == 'S') {
			sCnt++;
		}
		isVisited[x][y] = true;
		for(int i = 0; i < 4; i++) {
			int nx = x + dx[i];
			int ny = y + dy[i];
			if(nx < 0 || ny < 0 || nx >= 5 || ny >= 5)
				continue;
			if(isVisited[nx][ny]) continue;
			list.add(new int[] {nx, ny});
			isVisited[nx][ny] = true;
			DFS(nx, ny, r+1);
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token;
		
		// arr2d 초기화
		for(int i = 0; i < 5; i++) {
			String str = "";
			str += br.readLine();
			arr2d[i] = str.toCharArray();
		}
		
		//test 출력
		for(int i = 0; i < 5; i++) {
			System.out.println(arr2d[i]);
		}
		
		//각 원소마다 DFS 돌려보기
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 5; j++) {
				//초기화
				isVisited = new boolean[5][5];
				cnt = 0;
				sCnt = 0;
				list = new ArrayList<>();
				DFS(i, j, 1);
			}
		}
		System.out.println("result: " + result);

	}
}
