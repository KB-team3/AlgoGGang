import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B15565_�Ϳ�����̾� {
	static int N, K;
	static List<Integer> lion;

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		
		lion = new ArrayList<>();
		
		st = new StringTokenizer(bf.readLine());
		for (int i=0; i<N; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (num==1) lion.add(i); // ���̾� ������ ��� �ε����� ����
		}
		
		if(lion.isEmpty()||lion.size()<K-1) { // ���̾��� �ƿ� ���ų�, ���Ϸ��� ���������� ���� ���
			System.out.println(-1);
			return;
		}
		
		int min = Integer.MAX_VALUE; // �ּ� ���� ����
		for (int i=0; i<lion.size()-K+1; i++) {
			int size = lion.get(i+K-1) - lion.get(i) + 1; // ù��° ���̾���� ���鼭 K��° �������� �Ÿ����̸� ����
			min = (min<size)?min:size; // �ּҰ� ����
		}
		
		// ���
		System.out.println(min);
	}

}
