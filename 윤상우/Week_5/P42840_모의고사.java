package temp;

import java.util.ArrayList;
import java.util.List;

class Solution {

    static int [] sol1 ={1,2,3,4,5};
    static int [] sol2 ={2,1,2,3,2,4,2,5};
    static int [] sol3 ={3,3,1,1,2,2,4,4,5,5};

    public int[] solution(int[] answers) {
        int len = answers.length;

        int [] p = new int [4];

        for(int i=0; i<len; i++){
            if(answers[i] == sol1[i%5]) p[1]++;
            if(answers[i] == sol2[i%8]) p[2]++;
            if(answers[i] == sol3[i%10]) p[3]++;
        }

        int max = Math.max(p[1], Math.max(p[2], p[3]));

        List<Integer> answerList = new ArrayList<>();

        for(int i=1; i<4; i++){
            if(p[i] == max) answerList.add(i);
        }
        int size = answerList.size();
        int [] answer = new int [size];

        for(int i=0; i<size; i++){
            answer[i] = answerList.get(i);
        }

        return answer;
    }
}
public class P42840_모의고사 {
    public static void main(String[] args) {

    }
}
