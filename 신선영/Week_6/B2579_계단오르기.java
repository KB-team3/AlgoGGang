import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());   // 전체 계단의 수

        int[] stairs = new int[N];
        int[] DP = new int[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            stairs[i] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(Arrays.toString(stairs));

        // 전체 계단이 3개가 안되는 경우 예외 처리
        if (N <= 2) {
            int sum = 0;
            for (int i = 0; i < N; i++) {
                sum += stairs[i];
            }

            System.out.println(sum);
        }

        else {
            DP[0] = stairs[0];
            DP[1] = stairs[0] + stairs[1];
            // 1, 2, 3을 모두 밟을 수는 없음
            DP[2] = Math.max(stairs[1] + stairs[2], stairs[0] + stairs[2]);

            for (int i = 3; i < N; i++) {
                // 바로 이전 칸을 밟지 않을 경우와 이전 칸을 밟는 경우 비교
                DP[i] = Math.max(DP[i - 2] + stairs[i], DP[i - 3] + stairs[i - 1] + stairs[i]);
            }
            System.out.println(DP[N - 1]);
        }

    }
}
