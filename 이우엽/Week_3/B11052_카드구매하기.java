import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

class InfoPack implements Comparable<InfoPack> {
	int cnt;
	int price;
	double minEffec;
	InfoPack(int cnt, int price) {
		this.cnt = cnt;
		this.price = price;
		this.minEffec = getMinEffec();
	}
	public double getMinEffec() {
		return ((double)price) / cnt;
	}
	
	public int compareTo(InfoPack o) {
		if(this.minEffec > o.minEffec) {
			return -1;
		} else if(this.minEffec < o.minEffec) {
			return 1;
		}
		return 0;
	}
	
	public String toString() {
		return this.cnt + "개: " + this.price;
	}
}
public class B11052_카드구매하기 {
	static int N;
	static InfoPack[] arr;
	static List<Integer> list = new ArrayList<>();
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		// 가져야하는 카드 개수
		N = Integer.parseInt(br.readLine());
		arr = new InfoPack[N];
		
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		// N개만큼의 카드팩 정보 arr 초기화
		for(int i = 0; i < N; i++) {
			int price = Integer.parseInt(token.nextToken()); 
			InfoPack ip = new InfoPack(i+1, price);
			arr[i] = ip;
		}
		//test출력
		//System.out.println(Arrays.toString(arr));
		
		//먼저 사야하는 카드팩부터 정렬
		Arrays.sort(arr); 
		//test출력
		//System.out.println(Arrays.toString(arr));
		
		int idx = 0;
		while(N != 0) {
			if(idx == arr.length) {
				break;
			}
			InfoPack cur = arr[idx];
			int curCnt = cur.cnt;
			// 먼저 사야하는 카드의 개수와 전체 사야되는 카드의 개수가 같다면 
			if(curCnt == N) {
				list.add(cur.price);
				break;
			}
			// 먼저 사야하는 카드팩을 최대한 산다
			while (curCnt < N) {
				list.add(cur.price);
				N -= curCnt;
			}
			idx++;
		}
		//test 출력
		//System.out.println(list);
		int sum = 0;
		for(int i = 0; i < list.size(); i++) {
			sum += list.get(i);
		}
		System.out.println(sum);
	}
}
