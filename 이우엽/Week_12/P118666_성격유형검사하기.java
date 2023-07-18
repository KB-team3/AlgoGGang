import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        int[] scores = {-1, 3, 2, 1, 0, 1, 2, 3};
        Character[] types = {'R', 'T', 'C', 'F', 'J', 'M', 'A', 'N'};
        int[] scoreByTypes = {0, 0, 0, 0, 0, 0, 0, 0};
        for(int i = 0; i < choices.length; i++) {
            char type1 = survey[i].charAt(0);
            char type2 = survey[i].charAt(1);
            int type1Idx = Arrays.asList(types).indexOf(type1);
            int type2Idx = Arrays.asList(types).indexOf(type2);
            int choice = choices[i];
            switch(choice) {
                case 1, 2, 3:
                    scoreByTypes[type1Idx] += scores[choice];
                    break;
                case 5, 6, 7:
                    scoreByTypes[type2Idx] += scores[choice];
                    break;
                default:
                    break;
            }

        }
        for(int score : scoreByTypes) {
            System.out.println("score: " + score);
        }
        for(int i = 0; i < scoreByTypes.length; i = i + 2) {
            answer += scoreByTypes[i] >= scoreByTypes[i+1] ? types[i] : types[i+1];
        }
        return answer;

    }
}