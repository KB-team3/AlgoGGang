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

    public static void swap(char [] array, int i, int j){
        char temp = array[j];
        array[j] = array[i];
        array[i] = temp;
    }

    public static void main(String[] args) throws IOException {
        init();

        for(String s: arr){
            boolean isLast = true;
            char [] word = s.toCharArray();
            int len = word.length;
            int now = word.length - 1;

            for(int i= len-2; i>=0; i--){
                if(word[i] < word[now]){
                    isLast = false;
                    for(int j=len-1; j>i; j--){
                        if(word[j] > word[i]){
                            swap(word,i,j);
                            break;
                        }
                    }
                    Arrays.sort(word, i+1, len);
                    System.out.println(new String(word));
                    break;
                }else{
                    now = i;
                }
            }
            if(isLast) System.out.println(s);
        }

    }
}
