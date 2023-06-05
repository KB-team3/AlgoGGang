import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class StepInfo {
	int idx;
	int score;
	
	StepInfo(int idx, int score) {
		this.idx = idx;
		this.score = score;
	}
	
	public String toString() {
		return this.idx + " " + this.score; 
	}
}
public class B2579_계단오르기 {
	static int N;
	static int[] arr;
	static boolean[] isSelected;
	static int[] selection;
	static List<Integer> scoreList = new ArrayList<>();
	
	public static int calScore(List<StepInfo> list) {
		int sum = 0;
		for(int i = 0; i < list.size(); i++) {
			sum += list.get(i).score;
		}
		return sum;
	}
	public static boolean checkValid(List<StepInfo> list) {
		for(int i = 0; i < list.size()-2; i++) {
			if(list.get(i).idx + 1 == list.get(i+1).idx &&
					list.get(i+1).idx + 1 == list.get(i+2).idx) {
				return false;
			}
		}
		return true;
	}
	public static void subset(int num) {
		List<StepInfo> list = new ArrayList<>();
		//종료조건
		if(num >= N) {
			for(int i = 0; i < N; i++) {
				if(isSelected[i]) {
//					System.out.print(selection[i] + " ");
					StepInfo si = new StepInfo(selection[i], arr[i]);
					list.add(si);
				}
			}
			if(checkValid(list)) {
//				System.out.println("list: " + list);
				int score = calScore(list);
				scoreList.add(score);
			}
			return;
		}
		//분할
		isSelected[num] = true;
		selection[num] = num;
		subset(num+1);
		
		isSelected[num] = false;
		subset(num+1);
	}
	public static void solution() {
		subset(0);
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		arr = new int[N];
		isSelected = new boolean[N];
		selection = new int[N];
		
		for(int i = 0; i < 6; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		init();
//		System.out.println(Arrays.toString(arr));
		solution();
//		System.out.println("scoreList: " + scoreList);
		Collections.sort(scoreList, Collections.reverseOrder());
		System.out.println(scoreList.get(0));
	}
}
