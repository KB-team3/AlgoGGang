package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class TwoBall{
    int rx;
    int ry;
    int bx;
    int by;
    int count;

    TwoBall(int rx, int ry, int bx, int by, int count){
        this.rx = rx;
        this.ry = ry;
        this.bx = bx;
        this.by = by;
        this.count = count;
    }
}
public class B13460_구슬탈출2 {

    static int n;
    static int m;
    static int rx,ry,bx,by;
    static char [][] array;
    static int [] dx = {1,-1,0,0};
    static int [] dy = {0,0,1,-1};
    static boolean [][][][] isVisited;
    static int ans = -1;

    static void bfs(TwoBall twoBall){
        Queue<TwoBall> que = new ArrayDeque<>();
        que.offer(twoBall);

        isVisited[twoBall.rx][twoBall.ry][twoBall.bx][twoBall.by] = true;

        while(!que.isEmpty()){
            TwoBall now = que.poll();

            if(now.count > 10){
                ans = -1;
                return;
            }

            if(array[now.bx][now.by] == 'O') continue;

            if(array[now.rx][now.ry] == 'O'){
                ans = now.count;
                return;
            }

            for(int i=0; i<4; i++){

                int bx = now.bx;
                int by = now.by;

                while(true){
                    bx += dx[i];
                    by += dy[i];

                    if(array[bx][by] == 'O') break;
                    else if(array[bx][by] == '#'){
                        bx -= dx[i];
                        by -= dy[i];
                        break;
                    }
                }

                int rx = now.rx;
                int ry = now.ry;

                while(true){
                    rx += dx[i];
                    ry += dy[i];

                    if(array[rx][ry] == 'O') break;
                    else if(array[rx][ry] == '#'){
                        rx -= dx[i];
                        ry -= dy[i];
                        break;
                    }
                }

                if(bx==rx && by==ry && array[bx][by] != 'O'){
                    int dist_r = Math.abs(now.rx - rx) + Math.abs(now.ry - ry);
                    int dist_b = Math.abs(now.bx - bx) + Math.abs(now.by - by);

                    if(dist_r > dist_b){
                        rx -= dx[i];
                        ry -= dy[i];
                    }
                    else {
                        bx -= dx[i];
                        by -= dy[i];
                    }
                }

                if(isVisited[rx][ry][bx][by]) continue;

                isVisited[rx][ry][bx][by] = true;
                que.offer(new TwoBall(rx, ry, bx, by, now.count+1));
            }


        }
    }

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        array = new char[n][m];
        isVisited = new boolean[n][m][n][m];
        rx=0; ry=0; bx=0; by=0;

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for(int j=0; j<m; j++){
                array[i][j] = s.charAt(j);
                if(s.charAt(j)=='R'){
                    rx = i;
                    ry = j;
                }
                if(s.charAt(j)=='B'){
                    bx = i;
                    by = j;
                }

            }
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        bfs(new TwoBall(rx,ry,bx,by,0));
        System.out.println(ans);
    }
}
