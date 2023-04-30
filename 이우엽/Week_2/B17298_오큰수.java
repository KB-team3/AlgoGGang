package ct3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.TreeSet;

class Node implements Comparable<Node> {
	int value;
	int idx;
	
	Node(int value, int idx) {
		this.value = value;
		this.idx = idx;
	}
	public int compareTo(Node o) {
		return this.value - o.value;
	}
	public String toString() {
		return "" + this.value;
	}
}
public class B17298_오큰수 {
	static int[] arr;
	static TreeSet<Node> ts = new TreeSet<>();
	static int[] result;
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		
		arr = new int[N];
		result = new int[N];
		
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		// arr 초기화
		for(int i = 0; i < N; i++) {
			int value = arr[i] = Integer.parseInt(token.nextToken());
			int idx = i+1;
			Node node = new Node(value, idx);
			ts.add(node);
		}
		// test 출력
		// System.out.println(Arrays.toString(arr));
		// System.out.println("ts: " + ts);
		
		for(int i = 0; i < N; i++) {
			boolean checkValid = true;
			int value = arr[i];
			int idx = i+1;
			Node cur = new Node(value, idx);
			Node higher = ts.higher(cur);
			// 제일 가까운 값의 객체가 있지만 idx가 작으면
			while(higher != null && higher.idx < cur.idx) {
				higher = ts.higher(higher);
				// 제일 가까운 값의 객체가 없다면
				if(higher == null) {
					checkValid = false;
					// 탈출
					break;
				}
			}
			
			if(!checkValid || higher == null) {
				// System.out.println("-1");
				result[i] = -1;
				continue;
			}
			// System.out.println(higher);
			result[i] = higher.value;
		}
		// System.out.println(Arrays.toString(result));
		for(int i = 0; i < N; i++) {
			System.out.print(result[i] + " ");
		}
	}
}
