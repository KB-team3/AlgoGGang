package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B9081_단어맞추기 {
    static int n;
    static String [] arr;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        arr = new String[n];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            arr[i] = st.nextToken();
        }
    }

    public static void swap(int [] array, int i, int j){
        int temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }

    public static void main(String[] args) throws IOException {
        init();

        for(int i=0; i<n; i++){
            String alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            StringBuilder sb = new StringBuilder();
            int len = arr[i].length();
            int [] num = new int [len];

            for(int j=0; j<len; j++){
                for(int k=0; k<26; k++){
                    if(alphabet.charAt(k) == arr[i].charAt(j)){
                        num[j] = k;
                    }
                }
            }

            for(int start=len-1; start>=0; start--){
                boolean flag = false;

                for(int j=start-1; j>=0; j--){
                    if(num[j]<num[start]){
                        swap(num, j, start);
                        Arrays.sort(num, j+1, len);
                        flag = true;
                        break;
                    }
                }

                if(flag) break;
            }

            for(int n : num){
                sb.append(alphabet.charAt(n));
            }

            System.out.println(sb);
        }

    }
}
