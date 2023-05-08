package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B15565_귀여운라이언 {
    static int n;
    static int k;
    static int [] dolls;
    static int ans;
    static List<Integer> list;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        dolls = new int [n];
        st = new StringTokenizer(br.readLine());

        for(int i=0; i<n; i++){
            dolls[i] = Integer.parseInt(st.nextToken());
        }

        list = new ArrayList<>();
        ans = Integer.MAX_VALUE;
        for(int i=0; i<n; i++){
            if(dolls[i] == 1) {
                list.add(i);
            }
        }

        if(list.size() < k){
            System.out.println(-1);
            return;
        }

        for(int i=0; i<=list.size()-k; i++){

            ans = Math.min(ans, list.get(i+k-1) - list.get(i) +1);
        }

        System.out.println(ans);

    }
}
