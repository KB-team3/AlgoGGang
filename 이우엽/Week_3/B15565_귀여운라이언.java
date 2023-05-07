import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class B15565_귀여운라이언 {
	static int N;
	static int K;
	static int[] arr;
	static int[] acc1Sum;
	static int result;
	static List<Integer> list = new ArrayList<>();
	static List<Integer> gapList = new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		N = Integer.parseInt(token.nextToken());
		K = Integer.parseInt(token.nextToken());
		arr = new int[N+1];
		acc1Sum = new int[N+1];
		
		token = new StringTokenizer(br.readLine(), " ");
		//arr 초기화
		for(int i = 1; i < N+1; i++) {
			int cur = Integer.parseInt(token.nextToken());
			if(cur == 1) {
				arr[i] = cur;
			}
		}
		//test 출력
//		System.out.println(Arrays.toString(arr));
		
		//누적합 초기화
		for(int i = 1; i < N+1; i++) {
			acc1Sum[i] = arr[i] + acc1Sum[i-1];
		}
		//test 출력
		System.out.println(Arrays.toString(acc1Sum));
		
		int dupl = 0;
		for(int i = 1; i < N+1; i++) {
			if(dupl != acc1Sum[i]) {
				dupl = acc1Sum[i];
				list.add(i);
			}
		}
		//test출력
		System.out.println("list: " + list);
		if(list == null) {
			System.out.println("-1");
			return;
		}
		for(int i = list.size()-1; i >= 0; i--) {
			if(i-(K-1) < 0) {
				break;
			}
			int gap = list.get(i) - list.get(i-(K-1)) + 1; 
			gapList.add(gap);
		}
		//test출력
		System.out.println("gapList: " + gapList);
		if(gapList == null) {
			System.out.println("-1");
			return;
		}
		Collections.sort(gapList);
		System.out.println(gapList.get(0));
	}
}
