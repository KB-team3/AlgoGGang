class Solution {
    public static int answer;
    public static void DFS(int idx, int cur, int[] numbers, int target) {
        // 마지막 인덱스에 도달한 경우 타겟 넘버가 되는지 확인
        if (idx == numbers.length) {
            if (cur == target) {
                answer++;
            }
            return;
        }
        
        // 더하는 경우와 빼는 경우 각각 탐색
        DFS(idx + 1, cur - numbers[idx], numbers, target);
        DFS(idx + 1, cur + numbers[idx], numbers, target); 
    }
    
    public int solution(int[] numbers, int target) {
        answer = 0;
        DFS(0, 0, numbers, target);
        
        return answer;
    }
}
