import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long answer = 0;
        long left = 0;
        long right = times[times.length - 1] * (long) n;
        
        while (left <= right) {
            long mid = (left + right) / 2;
            long cnt = 0;   // 심사 받을 수 있는 사람 수
        
            for (int t : times) {
                cnt += mid / t;
            }
            
            if (cnt >= n) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        
        }
       return answer;
    }
}
