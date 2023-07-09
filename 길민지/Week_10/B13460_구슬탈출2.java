import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B13460_구슬탈출2 {
    static int N, M;
    static char[][] board;
    static int[] di = {1,-1,0,0};
    static int[] dj = {0,0,1,-1};
    public static void init() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        board = new char[N][M];
        for(int i=0; i<N; i++){
            String line = bf.readLine();
            for (int j=0; j<M; j++){
                board[i][j] = line.charAt(j);
            }
        }
    }

    public static void solution(){

    }


    public static void main(String args[]) throws IOException {
        init();
        solution();
    }
}
