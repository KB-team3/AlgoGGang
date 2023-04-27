package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class B17298_오큰수 {

    static int n;
    static String [] arr;
    static Stack<Integer> ans;
    static Stack<Integer> temp;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        n = Integer.parseInt(st.nextToken());
        ans = new Stack<>();
        temp = new Stack<>();

        arr = br.readLine().split(" ");

        for(int i=n-1; i>=0; i--){
            int num = Integer.parseInt(arr[i]);
            while(!temp.isEmpty() && num >= temp.peek()){
                temp.pop();
            }
            if(temp.isEmpty()){
                ans.add(-1);
            }else{
                ans.add(temp.peek());
            }
            temp.add(num);
        }


        while(!ans.isEmpty()){
            sb.append(ans.pop() + " ");
        }

        System.out.println(sb);
    }
}
