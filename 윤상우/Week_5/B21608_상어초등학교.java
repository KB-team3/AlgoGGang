package temp;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class B21608_상어초등학교 {

    static int n;
    static int [] studentList;
    static Map<Integer, List<Integer>> map;
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    static int[][] school ;
    static int answer;

    static void seat(int student){
        int nx, ny;
        int like, near;
        for(int x=0; x<n; x++){
            for(int y=0; y<n; y++){
                like = 0;
                near = 0;
                if(school[x][y] != 0) continue;

                for(int i=0; i<4; i++){
                    nx = x + dx[i];
                    ny = y + dy[i];

                    if(nx < 0 || nx >=n || ny <0 || ny >= n) continue;

                    List<Integer> likeList = map.get(student);
                    for(int n : likeList){
                        if(n == school[nx][ny]){
                            like++;
                        }

                        if(school[nx][ny] == 0){
                            near++;
                        }
                    }

                }

                // 값을 저장하는 방법을 모르겠음...
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        school = new int [n][n];
        studentList = new int [n*n];

        for(int i=0; i<n*n; i++){
            st = new StringTokenizer(br.readLine());
            int student = Integer.parseInt(st.nextToken());

            List<Integer> likeList = new ArrayList<>();

            for(int j=0; j<4; i++){
                likeList.add(Integer.parseInt(st.nextToken()));
            }

            studentList[i] = student;
            map.put(student,likeList);
        }

        for(int i=0; i<n*n; i++){
            seat(studentList[i]);
        }

        for(int x=0; x<n; x++){
            for(int y=0; y<n; y++){

            }
        }
    }
}
