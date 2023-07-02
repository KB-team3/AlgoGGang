import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class SensorInfo implements Comparable<SensorInfo> {
	int gap;
	int idx;
	
	SensorInfo(int gap, int idx) {
		this.gap = gap;
		this.idx = idx;
	}
	
	public String toString() {
		return idx + ": " + gap;
	}
	
	public int compareTo(SensorInfo o) {
		return o.gap - this.gap;
	}
} 
public class B2212_센서 {
	static int N;
	static int K;
	static int[] sensors;
	static SensorInfo[] sArr;
	static SensorInfo[] result;
	
	public static void cal() {
		for(int i = sensors.length-1; i > 0; i--) {
			int gap = sensors[i] - sensors[i-1];
			SensorInfo info =  new SensorInfo(gap, i);
			sArr[i] = info;
		}
		
		Arrays.sort(sArr, 1, sArr.length);
		System.out.println(Arrays.toString(sArr));
		
		result = Arrays.copyOfRange(sArr, 1, 1 + (K-1));
		System.out.println(Arrays.toString(result));
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		K = Integer.parseInt(br.readLine());
		
		sensors = new int[N];
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		for(int i = 0; i < N; i++) {
			sensors[i] = Integer.parseInt(token.nextToken());
		}
		
		sArr = new SensorInfo[N];
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
//		3  67  8  10  12  1415  18  20
		init();
		Arrays.sort(sensors);
		System.out.println(Arrays.toString(sensors));
		
		cal();	
	}
}
