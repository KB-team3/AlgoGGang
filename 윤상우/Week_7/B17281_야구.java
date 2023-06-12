package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class B17281_야구 {

    static int n;
    static int [][] array;

    static int [] selection;
    static boolean [] isSelected;
    static int ans;
    static int temp;

    static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());

        array = new int [n][9];
        isSelected = new boolean[9];
        selection = new int[9];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<9; j++){
                array[i][j] = Integer.parseInt(st.nextToken());
            }
        }

    }

//    static void go(Queue<Integer> que, int hit){
//        int size = que.size();
//        int i=0;
//        while(i<size){
//            int cur = que.peek()+hit;
//            if(cur<4) {
//                que.add(que.poll()+hit);
//            }else{
//                que.poll();
//                temp += 1;
//            }
//            i++;
//        }
//    }

    static void play(int [] selection){
        temp = 0;
        int o_cnt = 0;
        int inning = 0;
        int current = 0;
        boolean [] base = new boolean[4];
        Queue<Integer> que = new ArrayDeque<>();

        while(inning < n){

            if(o_cnt < 3){
                switch(array[inning][selection[current]]){
                    case 0:
                        o_cnt+=1;
                        break;
                    case 1:
//                        go(que, 1);
                        if(base[3]){
                            temp++;
                            base[3] = false;
                        }
                        if (base[2]) {
                            base[2] = false;
                            base[3] = true;
                        }
                        if (base[1]) {
                            base[1] = false;
                            base[2] = true;
                        }
                        base[1] = true;
//                        que.add(1);
                        break;
                    case 2:
//                        go(que, 2);
                        if(base[3]){
                            temp++;
                            base[3] = false;
                        }
                        if (base[2]) {
                            temp++;
                            base[2] = false;
                        }
                        if (base[1]) {
                            base[1] = false;
                            base[3] = true;
                        }
                        base[2] = true;
//                        que.add(2);
                        break;
                    case 3:
//                        go(que, 3);
                        if(base[3]){
                            temp++;
                            base[3] = false;
                        }
                        if (base[2]) {
                            temp++;
                            base[2] = false;
                        }
                        if (base[1]) {
                            temp++;
                            base[1] = false;
                        }
                        base[3] = true;
//                        que.add(3);
                        break;
                    case 4:
                        if(base[3]){
                            temp++;
                            base[3] = false;
                        }
                        if (base[2]) {
                            temp++;
                            base[2] = false;
                        }
                        if (base[1]) {
                            temp++;
                            base[1] = false;
                        }
                        temp++;
//                        temp += que.size() + 1;
//                        que = new ArrayDeque<>();
                        break;
                }
                if(current <8){
                    current+=1;
                }else{
                    current = 0;
                }

            }else{
                inning+=1;
                o_cnt = 0;
                base = new boolean[4];
//                que = new ArrayDeque<>();
            }
        }

        ans = Math.max(ans, temp);
    }

    static void dfs(int start){
        if(start == 3){
            selection[start] = 0;
            dfs(start+1);
        }
        if(start == 9){
            play(selection);
            return;
        }

        for(int i=1; i<9; i++){
            if(isSelected[i]) continue;
            isSelected[i] = true;
            selection[start] = i;
            dfs(start+1);
            isSelected[i] = false;
        }

    }

    public static void main(String[] args) throws IOException {
        init();
        dfs(0);
        System.out.println(ans);

    }
}
