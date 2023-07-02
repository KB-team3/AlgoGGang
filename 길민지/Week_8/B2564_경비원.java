import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2564_경비원 {
    static int W, H;
    static int N;
    static int stores[][];
    static int dg[];
    static int result;

    public static void init() throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        // 가로 세로 상점개수
        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());

        // 가게
        stores = new int[N][2];
        for(int i=0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            stores[i][0] = Integer.parseInt(st.nextToken());
            stores[i][1] = Integer.parseInt(st.nextToken());
        }

        // 동근
        st = new StringTokenizer(bf.readLine());
        dg = new int[2];
        dg[0] = Integer.parseInt(st.nextToken());
        dg[1] = Integer.parseInt(st.nextToken());
    }

    public static void solution(){
        for(int i=0; i<N; i++){
            int  dir = stores[i][0];
            int  pos = stores[i][1];

            if (dir == dg[0]){ // 둘이 같은 방향에 있을 때
                result += Math.abs(pos-dg[1]);
            }
            else if ((dir == 1 && dg[0] == 2) || (dir == 2 && dg[0] == 1)){ // 북&남
                result += H+Math.min(pos+dg[1], 2*W-pos-dg[1]);
            }
            else if ((dir == 3 && dg[0] == 4) || (dir == 4 && dg[0] == 3)){ // 동&서
                result += W+Math.min(pos+dg[1], 2*H-pos-dg[1]);
            }
            else if (dg[0] == 1){ // 동근 북
                if (dir == 3) result += dg[1]+pos; // 상점 서
                else result += W-dg[1]+pos; // 상점 동
            }
            else if (dg[0] == 2){ // 동근 남
                if (dir == 3) result += dg[1]+H-pos; // 상점 서
                else result += W-dg[1]+H-pos; // 상점 동
            }
            else if (dg[0] == 3){ // 동근 서
                if (dir == 1) result += dg[1]+pos; // 상점 북
                else result += H-dg[1]+pos; // 상점 남
            }
            else if (dg[0] == 4){ // 동근 동
                if (dir == 1) result += dg[1]+W-pos; // 상점 북
                else result += W-dg[1]+pos; // 상점 남
            }
        }
    }

    public static void main(String args[]) throws Exception{
        init();
        solution();
        System.out.println(result);
    }
}
