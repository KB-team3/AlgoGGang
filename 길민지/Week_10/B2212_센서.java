import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B2212_센서 {
    static int N, K;
    static int sensor[];
    static int dist[];
    static int result;

    public static void init() throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(bf.readLine());
        K = Integer.parseInt(st.nextToken());

        sensor = new int[N];
        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<N; i++){
            sensor[i] = Integer.parseInt(st.nextToken());
        }
    }

    public static void solution(){
        // 정렬
        Arrays.sort(sensor);

        // 센서 사이 거리 구하기
        dist = new int[N-1];
        for(int i=1; i<N; i++){
            dist[i-1] = sensor[i] - sensor[i-1];
        }

        // 작은 거리부터 더하기 (집중국 개수만큼 빼고)
        Arrays.sort(dist);
        for(int i=0; i<N-K;i++){
           result+=dist[i];
        }
    }

    public static void main(String args[]) throws IOException{
        init();
        solution();
        System.out.println(result);
    }
}
