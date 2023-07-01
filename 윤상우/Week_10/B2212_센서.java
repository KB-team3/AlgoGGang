package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class B2212_센서 {

    static int n;
    static int k;
    static int [] arr;
    static List<Integer> list;
    static int ans;


    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        arr = new int[n];
        ans = 0;
        list = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

    }

    public static void main(String[] args) throws IOException {
        init();
        Arrays.sort(arr);

        for(int i=0; i<n-1; i++){
            list.add(arr[i+1] - arr[i]);
        }

        Collections.sort(list, ((o1, o2) -> o2 - o1));

        for(int i=k-1; i<n-1; i++){
            ans += list.get(i);
        }

        System.out.println(ans);

    }
}
