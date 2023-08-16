import java.util.*;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int max_match_count = 0;
        int min_match_count = 0;
        int[] ranks = {6, 6, 5, 4, 3, 2, 1};
        for(int lotto : lottos) {
            System.out.println(lotto);
            if(lotto == 0) {
                max_match_count += 1;
            }

            for(int i = 0; i < win_nums.length; i++) {
                if(win_nums[i] == lotto) {
                    max_match_count += 1;
                    min_match_count += 1;
                    break;
                }
            }
        }
        int[] result = {ranks[max_match_count], ranks[min_match_count]};
        return result;
    }
}