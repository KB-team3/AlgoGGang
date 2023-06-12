import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B17281_야구 {
	static int N;
	static int[][] arr2d;
	static int outCnt;
	static int[] selection;
	static boolean[] isSelected;
	static int score;
	static int maxScore;
	static int total;
	public static int toScore(int num) {
		int score = 0;
		switch(num) {
		case 1:
			score += 1;
			break;
		case 2:
			score += 2;
			break;
		case 3:
			score += 3;
			break;
		case 4:
			score += 4;
			break;
		default:
			outCnt++;
			break;
		}
		return (int)Math.ceil(score/4.0);
	}
	public static void permutation(int r, int th) {
		//종료조건
		if(outCnt == 3) {
			
			for(int i = 0; i < 9; i++) {
				int cur = toScore(arr2d[th][selection[i]]);
//				System.out.print(cur);
				
				score += cur;
				
				if(score > maxScore) {
					maxScore = score;
				}
			}
			total += maxScore;
//			System.out.println();
			return;
		}
		
		if(r >= 9) {
			for(int i = 0; i < 9; i++) {
				int cur = toScore(arr2d[th][selection[i]]);
				score += cur;
			}
			selection = new int[9];
			isSelected = new boolean[9];
			permutation(0, th);
			return;
		}
		//재귀적 확장
		//4번 타석은 이미 결정
		if(r == 3) {
			isSelected[0] = true;
			selection[r] = 0;
			permutation(r+1, th);
			return;
		}
		// 2번선수부터 9번선수까지
		for(int i = 1; i < 9; i++) {
			if(isSelected[i]) continue;
			isSelected[i] = true;
			selection[r] = i;
			
			permutation(r+1, th);
			isSelected[i] = false;//백트래킹
		}
	}
	public static void solution() {
		for(int i = 0; i < N; i++) {
			selection = new int[9];
			isSelected = new boolean[9];
			outCnt = 0;
			score = 0;
			permutation(0, i);
		}
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr2d = new int[N][9];
		selection = new int[9];
		isSelected = new boolean[9];
		
		StringTokenizer token;
		
		for(int i = 0; i < N; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < 9; j++) {
				arr2d[i][j] = Integer.parseInt(token.nextToken());
			}
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		init();
		for(int i = 0; i < N; i++) {
			System.out.println(Arrays.toString(arr2d[i]));
		}
		solution();
		System.out.println("max Score: " + maxScore);
	}
}
