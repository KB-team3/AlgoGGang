import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1780_종이의개수__ver2 {
	static int N;
	static int[][] arr2d;
	static int cntM1;
	static int cnt0;
	static int cnt1;

	public static boolean checkValid(int x, int y, int size) {
		int std = arr2d[x][y];
		for(int i = x; i < x + size; i++) {
			for(int j = y; j < y + size; j++) {
				if(std != arr2d[i][j]) return false;
			}
		}
		return true;
	}
	public static void partition(int x, int y, int size) {
		if(checkValid(x, y, size)) {
			switch(arr2d[x][y]) {
			case -1:
				cntM1++;
				break;
			case 0:
				cnt0++;
				break;
			case 1:
				cnt1++;
				break;	
			}
			
			return;
		}
		
		int splitedSize = size / 3;
		partition(x, y, splitedSize);
		partition(x, y + splitedSize, splitedSize);
		partition(x, y + (2*splitedSize), splitedSize);
		
		partition(x + splitedSize, y, splitedSize);
		partition(x + splitedSize, y + splitedSize, splitedSize);
		partition(x + splitedSize, y + (2*splitedSize), splitedSize);
		
		partition(x + (2*splitedSize), y, splitedSize);
		partition(x + (2*splitedSize), y + splitedSize, splitedSize);
		partition(x + (2*splitedSize), y + (2*splitedSize), splitedSize);
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr2d = new int[N][N];
		StringTokenizer token;
		for(int i = 0; i < N; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < N; j++) {
				arr2d[i][j] = Integer.parseInt(token.nextToken());
			}
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		init();
		partition(0, 0, N);
		System.out.println(cntM1);
		System.out.println(cnt0);
		System.out.println(cnt1);
	}
}
