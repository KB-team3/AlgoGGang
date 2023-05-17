import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B14501_퇴사 {
	static int N;
	static int [] T, P;
	static int MAX = 0;
	
	public static void find(int day, int price) {
		if (day==N+1) { // N일까지 일을 마친 경우 
			MAX = (MAX>price)?MAX:price;
			return;
		}
		else if (day>N+1) { // N일까지 일을 마치지 못한 경우 
			return; 
		}
		
		// 오늘 일함
		find(day + T[day], price + P[day]);
		// 오늘 일 안 함 
		find(day+1, price);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(bf.readLine());
		
		// 입력 
		N = Integer.parseInt(st.nextToken());
		T = new int [N+1];
		P = new int [N+1];
		for (int i=1; i<N+1; i++) {
			st = new StringTokenizer(bf.readLine());
			T[i] = Integer.parseInt(st.nextToken());
			P[i] = Integer.parseInt(st.nextToken());
		}
		
		// 최대 수익 찾기 
		find(1, 0);
		
		// 출력 
		System.out.println(MAX);
	}

}
