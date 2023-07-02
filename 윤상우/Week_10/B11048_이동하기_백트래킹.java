package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11048_이동하기_백트래킹 {
    static int n;
    static int m;
    static int [][] array;
    static boolean [][] isVisited;
    static int [] dx = {1,0,1};
    static int [] dy = {0,1,1};
    static int ans = 0;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        array = new int [n][m];
        isVisited = new boolean[n][m];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<m; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    static boolean isValid(int x, int y){
        if(x<0 || x>=n || y<0 || y>=m) return false;
        return true;
    }
    static void dfs(int [] start){
        if(start[0] == n-1 && start[1] == m-1){
            ans = Math.max(ans, start[2]);
            return;
        }

        isVisited[start[0]][start[1]] = true;

        for(int i=0; i<3; i++){
            int next_x = start[0] + dx[i];
            int next_y = start[1] + dy[i];
            if(!isValid(next_x,next_y)) continue;
            if(isVisited[next_x][next_y]) continue;
            isVisited[next_x][next_y] = true;
            int candy = start[2] + array[next_x][next_y];
            dfs(new int []{next_x,next_y,candy});
            isVisited[next_x][next_y] = false;
        }
    }
    public static void main(String[] args) throws IOException {
        init();
        dfs(new int []{0,0,array[0][0]});
        System.out.println(ans);
    }
}
