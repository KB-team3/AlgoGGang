package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B1138_한줄로서기 {
    static int n;
    static int [] arr;
    static int [] selection;
    static boolean [] isVisited;
    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        arr = new int [n];
        selection = new int [n];
        isVisited = new boolean [n];

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++) arr[i] = Integer.parseInt(st.nextToken());
    }

    static void combination(int r){
        if(r==n){
            boolean flag = true;
            for(int i=n-1; i>=0; i--){
                int num =0;
                for(int j=i-1; j>=0; j--){
                    if(selection[i] < selection[j]) num++;
                }
                if(num != arr[selection[i]]){
                    flag = false;
                    break;
                }
            }
            if(flag) {
                for(int i=0; i<n; i++){
                    System.out.print(selection[i] + 1 + " ");
                }
            }
            return;
        }

        for(int i=0; i<n; i++){
            if(isVisited[i]) continue;
            selection[r] = i;
            isVisited[i] = true;
            combination(r+1);
            isVisited[i] = false;
        }
    }
    public static void main(String[] args) throws IOException {
        init();
        combination(0);

    }
}
