import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B17281_야구 {
    static int N;
    static int result[][];
    static int max;
    static int[] order;
    static boolean[] isSelected;

    // 입력 및 초기화
    public static void init() throws Exception{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(st.nextToken());
        result = new int [N][9];
        order = new int[9];
        isSelected = new boolean[9];

        for(int i=0; i<N; i++){
            st = new StringTokenizer(bf.readLine());
            for (int j=0; j<9; j++){
                result[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }

    // 해결
    public static void solution(){
        isSelected[0] = true;
        order[3]=0; // 4번 타자는 1번
        setOrder(0); // 타순 정하기
    }

    // 타순 정하기
    public static void setOrder(int num){
        if(num==3) { // 4번은 패스
            setOrder(num+1);
            return;
        }
        if(num==9){ // 타순 끝
            // 점수 구하기
            getScore(0, 0, 0);
            return;
        }
        for(int i=1; i<9; i++){
            if(isSelected[i]) continue;
            order[num] = i;
            isSelected[i] = true;
            setOrder(num+1);
            isSelected[i] = false;
        }
    }

    // 점수 구하기
    public static void getScore(int inning, int score, int start){
        if(inning==N){ // 게임 종료
            max = Math.max(max, score);
            return;
        }
        int out=0;
        int base[] = new int[4]; // 1루, 2루, 3루, 홈
        int batter = start;
        while(out<3){
            if(batter==9) batter=0;
            int batting = result[inning][order[batter++]];

            // 안타
            if(batting==1){
                base[3] += base[2];
                base[2] = base[1];
                base[1] = base[0];
                base[0] = 1;
            }
            // 2루타
            else if(batting==2){
                base[3] += base[2]+base[1];
                base[2] = base[0];
                base[1] = 1;
                base[0] = 0;
            }
            // 3루타
            else if(batting==3){
                base[3] += base[2]+base[1]+base[0];
                base[2] = 1;
                base[1] = 0;
                base[0] = 0;
            }
            // 홈런
            else if(batting==4){
                base[3] += base[2]+base[1]+base[0]+1;
                base[2] = 0;
                base[1] = 0;
                base[0] = 0;
            }
            // 아웃
            else{
                out++;
            }
        }
        getScore(inning+1, score+base[3], batter);
    }

    public static void main(String[] args) throws Exception {
        init();
        solution();
        System.out.println(max);
    }
}
