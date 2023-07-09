import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B11048_이동하기 {
    static int N, M;
    static int maze[][];
    static int temp[][];
    public static void init() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        maze = new int[N+1][M+1];
        temp = new int[N+1][M+1];
        for(int i=1; i<N+1; i++){
            st = new StringTokenizer(bf.readLine());
            for (int j=1; j<M+1; j++){
                maze[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    public static void solution(){
        for(int i=1; i<N+1; i++){
            for(int j=1; j<M+1; j++){
                int m1 = Math.max(temp[i-1][j], temp[i][j-1]);
                int m2 = Math.max(m1, temp[i-1][j-1]);
                temp[i][j] = m2 + maze[i][j];
            }
        }
    }

    public static void main(String args []) throws IOException{
        init();
        solution();
        System.out.println(temp[N][M]);
    }
}
