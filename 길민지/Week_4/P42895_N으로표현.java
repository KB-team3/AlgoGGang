import java.util.ArrayList;
import java.util.List;

class Solution {
    static int [] dp;
	static List<Integer>[] list;
	
	//범위 체크 
	public static boolean chkValid(int num) {
		if(num<=0 || num>32000) return false;
		return true;
	}
	
	// 처음 만나는 숫자라면 dp 배열에 저장하고, list에 추가 
	public static void cal(int calNum, int num) {
		if (chkValid(calNum) && dp[calNum]==0) {
			dp[calNum] = num;
			list[num].add(calNum);
		}
	}
	
	// num개의 숫자로 만들 수 있는 숫자 전부 구하기 
	public static void make(int N, int num) {
		// 2, 22, 222 같이 N을 num개 붙여서 만들 수 있는 숫자 추가 
		int n = 0;
		for (int i=0; i<num; i++) { 
			n += N * (int)Math.pow(10, i);
		}
		cal(n, num);
		
		// num개 이하의 숫자 2개를 합쳐서 만들 수 있는 모든 조합 
		for (int i=1; i<num; i++) {
			int j = num-i;
			for (int num1 : list[i]) {
				for (int num2 : list[j]) {
					// 사칙연산으로 만들 수 있는 숫자 추가 
					cal(num1+num2, num);
					cal(num1-num2, num);
					cal(num1/num2, num);
					cal(num1*num2, num);
				}
			}
		}
	}
    public int solution(int N, int number) {
        if (N==number) return 1; // N과 number가 같은 경우 
        dp = new int[32001]; // 각 숫자를 만드는 N 사용횟수 배열 
        
        list = new List[9];
        list[1] = new ArrayList<Integer>();
        list[1].add(N); // N 한개로 만들 수 있는 숫자는 N 하나 
        
        for (int i=2; i<9; i++) { // N 2개 ~ 8개로 만들 수 있는 숫자 리스트 만들기 
        	list[i] = new ArrayList<Integer>();
        	make(N, i);
        	if (dp[number]!=0) return dp[number]; // number를 만들었다면 return 
        }
        // 8개 이하로 만들 수 없는 경우 
        return -1;
    }
}

// Eclipse 테스트
/* 
public class P42895_N으로표현 {
	static int [] dp;
	static List<Integer>[] list;
	
	public static boolean chkValid(int num) {
		if(num<=0 || num>32000) return false;
		return true;
	}
	
	public static void cal(int calNum, int num) {
		if (chkValid(calNum) && dp[calNum]==0) {
			dp[calNum] = num;
			list[num].add(calNum);
		}
	}
	
	public static void make(int N, int num) {
		int n = 0;
		for (int i=0; i<num; i++) {
			n += N * (int)Math.pow(10, i);
		}
		cal(n, num);
		for (int i=1; i<num; i++) {
			int j = num-i;
			for (int num1 : list[i]) {
				for (int num2 : list[j]) {
					cal(num1+num2, num);
					cal(num1-num2, num);
					cal(num1/num2, num);
					cal(num1*num2, num);
				}
			}
		}
	}
	
	
	public static int solution(int N, int number) {
		if (N==number) return 1;
        dp = new int[32001];
        
        list = new List[9];
        list[1] = new ArrayList<Integer>();
        list[1].add(N);
        
        for (int i=2; i<9; i++) {
        	list[i] = new ArrayList<Integer>();
        	make(N, i);
        	if (dp[number]!=0) return dp[number];
        }
        
        return -1;
    }

	public static void main(String[] args) {
		System.out.println(solution(2, 2));
	}
}
*/
