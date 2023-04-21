package BackTracking;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class B15686_치킨배달 {
    static int n;
    static int m;
    static int [][] map;
    static boolean [] isSelected;
    static List<int []> chickens;
    static List<int []> homes;
    static int answer;
    static int temp_ans;
    static int temp;

    static void select(int n, int start){
        if(n==m){
            temp_ans=0;
            for(int i=0; i<homes.size(); i++) {
                temp = Integer.MAX_VALUE;
                for(int j=0; j<isSelected.length; j++){
                    if(isSelected[j]) {
                        temp = Integer.min(temp,distance(homes.get(i),chickens.get(j)));
                    }
                }
                temp_ans += temp;
            }
            answer = Integer.min(temp_ans, answer);
        }
        for(int i=start; i<chickens.size(); i++){
            if(isSelected[i]) continue;
            isSelected[i] = true;
            select(n+1,i+1);
            isSelected[i] = false;
        }
    }

    static int distance(int a [], int b []){
        return Math.abs(a[0] - b[0]) + Math.abs(a[1]- b[1]);
    }



    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][n];

        for(int i=0; i<n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        homes = new ArrayList<>();
        chickens = new ArrayList<>();

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(map[i][j] == 1) homes.add(new int[]{i,j});
                if(map[i][j] == 2) chickens.add(new int[]{i,j});
            }
        }

        isSelected = new boolean[chickens.size()];
        answer = Integer.MAX_VALUE;
        select(0,0);

        System.out.println(answer);

    }
}
