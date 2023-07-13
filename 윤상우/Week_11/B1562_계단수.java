package temp;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class B1562_계단수 {
    static int N;
    static int ans;
    static boolean [] isVisited;
    static int [] selection;
    static void dfs(int r){
        if(r==N){
            boolean flag1 = true;
            boolean flag2 = true;

            for(int i=0; i<10; i++){
                if(!isVisited[i]){
                    flag1 = false;
                    break;
                }
            }

            for(int i=0; i<N-1; i++){
                if(selection[i+1] != selection[i] +1 || selection[i+1] != selection[i] -1){
                    flag2 = false;
                    break;
                }
            }

            if(flag1 && flag2){
                ans++;
            }
            return;
        }

        if(r==0){
            for(int i=1; i<10; i++){
                selection[r] = i;
                isVisited[i] = true;
                dfs(r+1);
                isVisited[i] = false;
            }
        }else{
            for(int i=0; i<10; i++){
                selection[r] = i;
                isVisited[i] = true;
                dfs(r+1);
                isVisited[i] = false;
            }
        }

    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        ans = 0;
        isVisited = new boolean[10];
        selection = new int [N];
        dfs(0);
        System.out.println(ans);
    }
}
