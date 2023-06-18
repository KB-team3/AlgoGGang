import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2564_경비원 {
	static int w;
	static int h;
	static int num;
	static int[][] coords;
	static int x;
	static int y;
	static int[] result;
	public static void findClosest(int idx, int direc, int dist) {
		//현재위치와 상점의 방향이 같을 때
		if(x == direc) {
			result[idx] = Math.abs(dist - y);
			return;
		}
		//방향이 같지 않을때
		//북남, 서동
		if(Math.abs(x-direc) == 1 && (x != 2 || direc != 2)) {
			if(x == 1 || x == 2) {
				if(y + dist < (w-y) + (w-dist)) {
					result[idx] = y + dist + h;
				} else {
					result[idx] = (w-y) + (w-dist) + h;
				}
			} else {
				if(y + dist < (h-y) + (h-dist)) {
					result[idx] = y + dist + w;
				} else {
					result[idx] = (h-y) + (h-dist) + w;
				}
			}
			return;
		} else { 
			
		}
	}
	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer token = new StringTokenizer(br.readLine(), " ");
		w = Integer.parseInt(token.nextToken());
		h = Integer.parseInt(token.nextToken());
		num = Integer.parseInt(br.readLine());
		coords = new int[num][2];
		result = new int[3];
		for(int i = 0; i < num; i++) {
			token = new StringTokenizer(br.readLine(), " ");
			coords[i][0] = Integer.parseInt(token.nextToken()); //1:북 2:남 3:서 4:동
			coords[i][1] = Integer.parseInt(token.nextToken());
		}
		token = new StringTokenizer(br.readLine(), " ");
		x = Integer.parseInt(token.nextToken());
		y = Integer.parseInt(token.nextToken());
	}
	public static void main(String[] args) throws IOException {
		init();
		for(int i = 0; i < num; i++) {
			System.out.println(Arrays.toString(coords[i]));
		}
		//solution
		for(int i = 0; i < num; i++) {
			findClosest(i, coords[i][0], coords[i][1]);
		}
		

	}
}
