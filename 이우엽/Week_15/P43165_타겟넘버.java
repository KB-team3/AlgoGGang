class Solution {
    int result = 0;

    public void DFS(int[] numbers, int target, int index, int sum) {
        if(index == numbers.length) {
            if(sum == target) {
                result++;
            }
            return;
        }

        DFS(numbers, target, index+1, sum+numbers[index]);
        DFS(numbers, target, index+1, sum-numbers[index]);
    }

    public int solution(int[] numbers, int target) {
        int answer = 0;
        DFS(numbers, target, 0, 0);

        answer = result;
        return answer;
    }
}