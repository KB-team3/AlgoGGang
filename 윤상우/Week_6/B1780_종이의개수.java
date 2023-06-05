package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1780_종이의개수 {
    static int n;
    static int zero_n;
    static int plus_n;
    static int minus_n;
    static int [][] array;

    static void find(int [] start, int N){
        int target = array[start[0]][start[1]];
        boolean flag = true;

        // 정복
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if (target != array[start[0]+i][start[1]+j]){
                    flag = false;
                    break;
                }
            }
        }

        if(flag){
            if(target ==0) zero_n++;
            if(target ==-1) minus_n++;
            if(target ==1) plus_n++;
        }else{
            for(int i=0; i<3; i++){
                for(int j=0; j<3; j++){
                    int [] new_start = {start[0] + (N/3)*i, start[1] + (N/3)*j};
                    find(new_start, N/3);
                }
            }
        }


    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        array = new int [n+1][n+1];

        for(int i=1; i<=n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=1; j<=n; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int [] start = {1,1};

        find(start, n);

        System.out.println(minus_n);
        System.out.println(zero_n);
        System.out.println(plus_n);

    }
}
