package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B1941_소문난칠공주 {
    static int ans;
    static char [][] table;
    static boolean [] isVisited;
    static int [] isSelected;
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,-1,1};
    static boolean isValid(int x, int y){
        if(x<0 || x>=5 || y<0 || y>=5) return false;
        return true;
    }

    static void select(int start, int cnt, int cntS){
        if(cnt - cntS > 3) return; // 다솜파가 4 이상이 못되는 경우 cut

        if(cnt == 7){
            isVisited = new boolean[7]; // 선택한 7개 방문 처리 배열 초기화
            bfs(isSelected[0]); // 뽑은 7개에 대해 bfs
            return;
        }

        for(int i=start; i<25; i++){
            int row = i / 5;
            int col = i % 5;
            isSelected[cnt] = i;
            select(i+1, cnt+1, table[row][col] == 'S'?cntS+1:cntS);
        }
    }

    static void bfs(int n){
        int num =1;
        isVisited[0] = true;
        Queue<Integer> que = new ArrayDeque<>();
        que.offer(n);

        while(!que.isEmpty()){
            int now = que.poll();
            int nowX = now / 5;
            int nowY = now % 5;

            for(int i=0; i<4; i++){
                int nextX = nowX + dx[i];
                int nextY = nowY + dy[i];
                if(!isValid(nextX, nextY)) continue;
                int next = nextX * 5 + nextY;

                for(int j=0; j<7; j++){
                    if(!isVisited[j] && isSelected[j] == next){
                        // 방문하지 않고, 뽑은 곳이 이어진 경우
                        isVisited[j] = true;
                        num++;
                        que.offer(next);
                    }
                }

            }
        }
        if(num==7) ans++; // 7개 모두 이어진 경우 정답 올리기
    }

    public static void main(String[] args) throws IOException {
        // 조건
        // 1. 7개 뽑기 -> select
        // 2. 인접한지 확인 -> bfs
        // 3. s >=4 (4,5,6,7) -> select 종료 조건
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        table = new char [5][5];
        isSelected = new int [7];

        for(int i=0; i<5; i++){
            String s = br.readLine();
            for(int j=0; j<5; j++){
                table[i][j] = s.charAt(j);
            }
        }

        ans = 0;

        select(0,0,0);

        System.out.println(ans);

    }
}
