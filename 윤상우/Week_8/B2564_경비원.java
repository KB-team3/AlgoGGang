package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B2564_경비원 {
    static int [][] arr;

    static int x;
    static int y;
    static int n;
    static int [] target;
    static int ans;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        arr = new int [n][2];
        target = new int [2];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i][0] = Integer.parseInt(st.nextToken());
            arr[i][1] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        target[0] = Integer.parseInt(st.nextToken());
        target[1] = Integer.parseInt(st.nextToken());

        ans = 0;
    }
    public static void main(String[] args) throws IOException {
        init();

        for(int i=0; i<n; i++){
            switch (target[0]){
                case 1:
                    switch (arr[i][0]){
                        case 1:
                            ans += Math.abs(arr[i][1] - target[1]);
                            break;
                        case 2:
                            ans += Math.min(arr[i][1] + target[1] + y, 2 * x - (arr[i][1] + target[1]) +y);
                            break;
                        case 3:
                            ans += target[1] + arr[i][1];
                            break;
                        case 4:
                            ans += (x - target[1]) + arr[i][1];
                            break;

                    }
                    break;
                case 2:
                    switch (arr[i][0]){
                        case 1:
                            ans += Math.min(arr[i][1] + target[1] + y, 2 * x - (arr[i][1] + target[1]) +y);
                            break;
                        case 2:
                            ans += Math.abs(arr[i][1] - target[1]);
                            break;
                        case 3:
                            ans += target[1] + y - arr[i][1];
                            break;
                        case 4:
                            ans += (x - target[1]) + (y - arr[i][1]);
                            break;

                    }
                    break;
                case 3:
                    switch (arr[i][0]){
                        case 1:
                            ans += arr[i][1] + target[1];
                            break;
                        case 2:
                            ans += arr[i][1] + y - target[1];
                            break;
                        case 3:
                            ans += Math.abs(arr[i][1] - target[1]);
                            break;
                        case 4:
                            ans += Math.min(arr[i][1] + target[1] + x, 2 * y - (arr[i][1] + target[1]) +x);
                            break;

                    }
                    break;
                case 4:
                    switch (arr[i][0]){
                        case 1:
                            ans += (x - arr[i][1]) + target[1];
                            break;
                        case 2:
                            ans += (x - arr[i][1]) + y - target[1];
                            break;
                        case 3:
                            ans += Math.min(arr[i][1] + target[1] + x, 2 * y - (arr[i][1] + target[1]) +x);
                            break;
                        case 4:
                            ans += Math.abs(arr[i][1] - target[1]);
                            break;

                    }
                    break;
            }
        }
        System.out.println(ans);
    }
}
