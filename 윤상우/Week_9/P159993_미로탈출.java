package temp;

import java.util.ArrayDeque;
import java.util.Queue;

public class P159993_미로탈출 {
    static char [][] arr;
    static boolean [][] isVisited;
    static int x;
    static int y;
    static int [] dx = {-1,1,0,0};
    static int [] dy = {0,0,-1,1};
    static int answer;
    static int goToLev;
    static int goToExit;

    public static boolean checkValid(int now_x, int now_y){
        if(now_x < 0 || now_x >= x || now_y <0 || now_y >= y){
            return false;
        }
        return true;
    }

    public static void bfs(int [] start, char target){
        Queue<int []> que = new ArrayDeque<>();
        que.add(start);
        isVisited[start[0]][start[1]] = true;

        while(!que.isEmpty()){
            int [] now = que.poll();
            int now_x = now[0];
            int now_y = now[1];
            int step = now[2];

            if(arr[now_x][now_y] == target){
                if(target == 'L'){
                    goToLev = step;
                    answer += goToLev;
                }else if(target == 'E'){
                    goToExit = step;
                    answer += goToExit;
                }
                break;
            }

            for(int i=0; i<4; i++){
                int next_x = now_x + dx[i];
                int next_y = now_y + dy[i];
                if(!checkValid(next_x, next_y)) continue;
                if(isVisited[next_x][next_y]) continue;
                if(arr[next_x][next_y] == 'X') continue;

                que.add(new int [] {next_x, next_y, step+1});
                isVisited[next_x][next_y] = true;
            }
        }


    }
    public static int solution(String[] maps) {
        answer = 0;

        x = maps.length;
        y = maps[0].length();

        arr = new char [x][y];

        int [] start = {};
        int [] lev = {};

        for(int i=0; i<x; i++){
            for(int j=0; j<y; j++){
                arr[i][j] = maps[i].charAt(j);
                if(arr[i][j] == 'S') start = new int [] {i,j,0};
                if(arr[i][j] == 'L') lev = new int [] {i,j,0};
            }
        }

        isVisited = new boolean [x][y];
        bfs(start, 'L');

        isVisited = new boolean [x][y];
        bfs(lev, 'E');

        if(goToLev == 0 || goToExit == 0) return -1;

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(solution(new String []{"SLXOX", "EXXXO", "OOOOO", "OXXXX", "OOOOO"}));
    }
}
