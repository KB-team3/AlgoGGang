package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B2212_센서_백트래킹 {

    static int n;
    static int k;
    static int [] arr;
    static int [] selection;
    static boolean [] ischecked;
    static int ans = Integer.MAX_VALUE;


    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        selection = new int[n];

        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

    }

        static void combi(int s, int r){
        if(r==n){
            ischecked = new boolean[k+1];
            for(int i=0; i<n; i++){
                ischecked[selection[i]] = true;
            }

            for(int i=1; i<=k; i++){
                if(!ischecked[i]) return;
            }

            int min_temp = arr[0];
            int temp = 0;
            for(int i=0; i<n-1; i++){
                if(selection[i] != selection[i+1]) {
                    temp += arr[i] - min_temp;
                    min_temp = arr[i+1];
                }
                if(i == n-2){
                    temp += arr[n-1] - min_temp;
                }
            }

            ans = Math.min(ans, temp);

            return;
        }

        for(int i=s; i<=k; i++){
            selection[r] = i;
            combi(i,r+1);
        }
    }
    public static void main(String[] args) throws IOException {
        init();
        Arrays.sort(arr);
        combi(1,0);
        System.out.println(ans);
    }
}
