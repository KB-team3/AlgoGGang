package temp;

public class P42895_N으로표현 {
    static int [] array;
    static int [] dp;
    static int cnt;

    public static boolean isValid(int n){
        if(n > 32000 || n < 1) return false;
        return true;
    }
    public static void dfs(int now , int cnt){
        if(cnt >7) return;

        int next;
        for(int i : array){
            if(i == 1){
                next = now + now;
                if(!isValid(next)) continue;
                dp[next] = dp[now] + 1;
                dfs(next, cnt+1);
            }else if (i == 2){
                next = now - now;
                if(!isValid(next)) continue;
                dp[next] = dp[now] + 1;
                dfs(next, cnt+1);
            }else if (i == 3){
                next = now * now;
                if(!isValid(next)) continue;
                dp[next] = dp[now] + 1;
                dfs(next, cnt+1);
            }else if (i == 4){
                next = now / now;
                if(!isValid(next)) continue;
                dp[next] = dp[now] + 1;
                dfs(next, cnt+1);
            }else{
                next = now + 10*now;
                if(!isValid(next)) continue;
                dp[next] = dp[now] + 1;
                dfs(next, cnt+1);
            }
        }

    }
    public int solution(int N, int number) {
        int answer = 0;
        dp = new int [32000];
        array = new int[]{1,2,3,4,5};
        dp[N] = 1;

        dfs(N,0);
        answer = dp[number];
        return answer;
    }
}
