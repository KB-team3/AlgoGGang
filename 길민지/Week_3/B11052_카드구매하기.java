import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11052_ī�屸���ϱ� {
	static int N;
	static int P[];
	static int MAX[];
	
	public static void main (String [] args) throws NumberFormatException, IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// �Է� �� �ʱ�ȭ
		N = Integer.parseInt(st.nextToken());
		P = new int [N+1];
		MAX = new int [N+1];
		
		st = new StringTokenizer(bf.readLine());
		for (int i=1; i<N+1; i++) {
			P[i] = Integer.parseInt(st.nextToken());
		}
		
		// MAX[i]�� i�� �� �� ���� ��� ������ �����ϴ� �迭
		MAX[1] = P[1];
		
		for (int i=2; i<=N; i++) { // MAX[2] ~ MAX[N] ���ϱ�
			int max = 0;
			for (int j=1; j<=i/2; j++) { // i/2 ���ĺ��ʹ� �ߺ����� ���ϴ°Ŵϱ� �� ���Ƶ� ��
				max = Math.max(max, MAX[j] + MAX[i-j]);
			}
			max = Math.max(max, P[i]);
			MAX[i] = max;
		}
		
		// ���
		System.out.println(MAX[N]);
	}
}
