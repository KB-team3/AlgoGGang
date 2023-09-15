package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B16236_아기상어 {
    static int N;
    static int [][] arr;
    static int x;
    static int y;
    static int [] dx={-1,1,0,0};
    static int [] dy={0,0,-1,1};
    static int kg=2;
    static int answer=0;
    static int ate=0;
    public static List<int[]> bfs(int x, int y){
        List<int[]> list = new ArrayList<>();
        int [][] visited = new int[N][N];
        Queue<int []> que = new ArrayDeque<>();
        que.add(new int[]{x,y});

        while(!que.isEmpty()){
            int [] now = que.poll();
            int cx = now[0]; int cy = now[1];
            for(int i=0; i<4; i++){
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if(nx<0 || nx>=N || ny<0 || ny>=N) continue;
                if(visited[nx][ny]>0) continue;
                if(arr[nx][ny]>kg) continue;

                visited[nx][ny]=visited[cx][cy]+1;
                if(arr[nx][ny]<kg && arr[nx][ny]>0) {
                    list.add(new int[]{visited[nx][ny], nx, ny});
                }
                que.add(new int[]{nx,ny});
            }
        }

        return list;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        arr = new int [N][N];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<N; j++){
                int fish = Integer.parseInt(st.nextToken());
                if(fish==9){
                    arr[i][j] = 0;
                    x=i; y=j;
                    continue;
                }
                arr[i][j] = fish;
            }
        }

        while(true){
            List<int[]> temp = bfs(x,y);
            if(temp.isEmpty()){
                break;
            }

            Collections.sort(temp, (o1,o2)-> o1[0]!=o2[0]? o1[0]-o2[0]:
                    o1[1]!=o2[1]? o1[1]-o2[1]:o1[2]-o2[2]);

            int [] now = temp.get(0);
            answer+=now[0];
            x=now[1]; y=now[2];
            arr[x][y]=0;
            ate++;

            if(kg==ate){
                kg++;
                ate=0;
            }

        }

        System.out.println(answer);

    }
}
