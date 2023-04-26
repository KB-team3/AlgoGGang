import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B16948_��������Ʈ{
	static int N;
	static int r1, c1, r2, c2;
	static int dr[] = {-2, -2, 0, 0, 2, 2};
	static int dc[] = {-1, 1, -2, 2, -1, 1};
	static boolean [][] selected;
	
	// ���� üũ
	public static boolean validChk(int r, int c) {
		if (r<0 || c<0 || r>N-1 || c>N-1) return false;
		return true;
	}
	
	public static int BFS() {
		Queue <Integer[]> que = new ArrayDeque<>();
		que.add(new Integer[] {r1, c1, 0}); // ������ �߰�
		selected[r1][c1] = true;
		
		while(!que.isEmpty()) {
			int now_r = que.peek()[0];
			int now_c = que.peek()[1];
			int now_d = que.poll()[2];
			
			// 6�� Ž��
			for(int i=0; i<6; i++) {
				int next_r = now_r + dr[i];
				int next_c = now_c + dc[i];
				int next_d = now_d + 1;
				
				if(next_r == r2 && next_c == c2) { // �̵� �Ϸ�
					return next_d;
				}
				
				// ��ȿ�� üũ
				if(!validChk(next_r, next_c)||selected[next_r][next_c]) continue;
				que.add(new Integer[] {next_r, next_c, next_d}); // ���� ��ġ �߰�
				selected[next_r][next_c] = true;
			}
		}
		
		return -1;
	}
	
	public static void main(String [] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// �Է�
		N = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(bf.readLine());
		r1 = Integer.parseInt(st.nextToken());
		c1 = Integer.parseInt(st.nextToken());
		r2 = Integer.parseInt(st.nextToken());
		c2 = Integer.parseInt(st.nextToken());
		
		// �迭 �ʱ�ȭ
		selected = new boolean[N][N];
		
		// ���� ���
		System.out.println(BFS());
	}
	
}
