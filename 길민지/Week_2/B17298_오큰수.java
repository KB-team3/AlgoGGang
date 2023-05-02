import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class B17298_오큰수 {
	static int N;
	static int result[];
	static Stack<Integer[]> stack;
	
	public static void main(String [] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// 첫째줄 입력
		N = Integer.parseInt(st.nextToken());
		
		// 초기화
		result = new int[N];
		stack = new Stack<Integer[]>();
		
		// 수열 입력
		st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			result[i] = -1;
			
			while(!stack.isEmpty() && stack.peek()[1]<num) { 
				// 스택에 현재 값보다 작은 값이 있다면 그 자리에 현재 값 저장
				result[stack.pop()[0]] = num;
			}
			stack.add(new Integer[] {i, num}); // 현재 인덱스, 값 push
		}
		
		// 출력
		StringBuilder sb = new StringBuilder();
		for(int i : result) sb.append(i).append(" ");
		System.out.println(sb);
	}
}
