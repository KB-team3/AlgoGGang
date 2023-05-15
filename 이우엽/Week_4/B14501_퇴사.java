import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class MeetInfo {
	int period;
	int price;
	MeetInfo(int period, int price) {
		this.period = period;
		this.price = price;
	}
	public String toString() {
		return this.period + " " + this.price;
	}
}
public class B14501_퇴사 {
	static int N;
	static List<MeetInfo> list = new ArrayList<>();
	static boolean[] isSelected;
	static int next;
	static List<Integer> priceList = new ArrayList<>();
	public static void subset(int day) {
		//1일(0)부터 ~ N일(N-1)까지의 정보만
		if(day > N-1) {
			return;
		}
		
		MeetInfo cur = list.get(day);

		//종료조건, 요일+기간 > 퇴사일일때,
		if(day + cur.period > N-1) {
			int priceSum = 0;
			for(int i = 0; i < N; i++) {
				if(isSelected[i]) {
					System.out.println("day: " + (i+1));
					priceSum += list.get(i).price;
				}
			}
			priceList.add(priceSum);
			System.out.println("------");
			return;
		}
		
		//분할
		isSelected[day] = false;
		next = day+1;
		subset(next);
		
		isSelected[day] = true;
		next = day + cur.period;
		subset(next);
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		//N일
		N = Integer.parseInt(br.readLine());
		isSelected = new boolean[N];
		StringTokenizer token;
		//N일동안의 상담정보 초기화
		for(int i = 0; i < N; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			int period = Integer.parseInt(token.nextToken());
			int price = Integer.parseInt(token.nextToken());
			MeetInfo mi = new MeetInfo(period, price);
			list.add(mi);
		}
		//test 출력
//		for(int i = 0; i < N; i++) {
//			System.out.println(list.get(i));
//		}
		
		//1일부터시작
		subset(0);
		
		System.out.println("priceList: " + priceList);

	}
}
