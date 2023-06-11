import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B1932_정수삼각형 {
	static int N;
	static List<Integer>[] tree;
	static boolean[][] isSelected;
	static int maxSum;
	
	public static void selectChild(int r, int node) {
		if(r == N) {
			int sum = 0;
			for(int i = 0; i < N; i++) {
//				System.out.print(i + ": ");
				for(int j = 0; j < tree[i].size(); j++) {
					if(isSelected[i][j]) {
//						System.out.print(tree[i].get(j) +" ");
						sum += tree[i].get(j);
					}
				}
//				System.out.println();
			}
//			System.out.println("sum: " + sum);
			if(sum > maxSum) {
				maxSum = sum;
			}
			return;
		}
		
		if(r == 0) {
			isSelected[r][node] = true;
			selectChild(r+1, node);
			return;
		}
		
		isSelected[r][node] = true;
		selectChild(r+1, node);
		isSelected[r][node] = false;
		
		isSelected[r][node+1] = true;
		selectChild(r+1, node+1);
		isSelected[r][node+1] = false;
	}
	public static void solution() {
		selectChild(0,0);
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		tree = new ArrayList[N];
		for(int i = 0; i < N; i++) {
			tree[i] = new ArrayList<>();
		}
		isSelected = new boolean[N][500];
		
		StringTokenizer token;
		for(int i = 0; i < N; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			for(int j = 0; j < i+1; j++) {
				tree[i].add(Integer.parseInt(token.nextToken()));
			}
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		init();
//		for(int i = 0; i < N; i++) {
//			System.out.println(tree[i]);
//		}
		solution();
		System.out.println(maxSum);
	}
}