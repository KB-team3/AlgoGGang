package BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B16948_데스나이트 {
    static int n;
    static int [][] arr;
    static boolean [][] isVisited;
    static int [] start;
    static int [] end;
    static int [] dx = {-2,-2,0,0,2,2};
    static int [] dy = {-1,1,-2,2,-1,1};

    static boolean isValid(int x, int y){
        if(x<0 || x>=n || y<0 || y>=n) return false;
        return true;
    }

    static void bfs(int [] start){
        Queue<int []> que = new ArrayDeque<>();
        que.add(start);
        isVisited[start[0]][start[1]] = true;

        while(!que.isEmpty()){
            int [] now = que.poll();
            int now_x = now[0];
            int now_y = now[1];
            for(int i=0; i<6; i++){
                int next_x = now_x + dx[i];
                int next_y = now_y + dy[i];
                if(!isValid(next_x, next_y)) continue;
                if(isVisited[next_x][next_y]) continue;
                que.add(new int [] {next_x, next_y});
                isVisited[next_x][next_y] = true;
                arr[next_x][next_y] = arr[now_x][now_y] + 1;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        arr = new int[n][n];
        start = new int[2];
        end = new int[2];
        isVisited = new boolean[n][n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<4; i++){
            if(i<2) start[i] = Integer.parseInt(st.nextToken());
            else end[i-2] = Integer.parseInt(st.nextToken());
        }

        bfs(start);

        if(arr[end[0]][end[1]] == 0){
            System.out.println(-1);
        }else{
            System.out.println(arr[end[0]][end[1]]);
        }


    }
}
