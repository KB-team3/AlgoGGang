import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class B17298_��ū�� {
	static int N;
	static int result[];
	static Stack<Integer[]> stack;
	
	public static void main(String [] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// ù°�� �Է�
		N = Integer.parseInt(st.nextToken());
		
		// �ʱ�ȭ
		result = new int[N];
		stack = new Stack<Integer[]>();
		
		// ���� �Է�
		st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			result[i] = -1;
			
			while(!stack.isEmpty() && stack.peek()[1]<num) { 
				// ���ÿ� ���� ������ ���� ���� �ִٸ� �� �ڸ��� ���� �� ����
				result[stack.pop()[0]] = num;
			}
			stack.add(new Integer[] {i, num}); // ���� �ε���, �� push
		}
		
		// ���
		StringBuilder sb = new StringBuilder();
		for(int i : result) sb.append(i).append(" ");
		System.out.println(sb);
	}
}
