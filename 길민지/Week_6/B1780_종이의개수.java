import java.util.*; 
import java.io.*;

class Main {
  static int N;
  static int [][] matrix;
  static int [] cnt; // -1, 0, 1의 개수

  static void cut(int[] start, int n){
    int num = matrix[start[0]][start[1]]; // 첫번째 숫자
    boolean isSame = true; // 다 같은 수인지
    for (int i=0; i<n; i++){
      for(int j=0; j<n; j++){
        if (matrix[start[0]+i][start[1]+j] != num){ 
          isSame = false;
          break;
        }
      }
    }

    if (isSame){ // 전부 같은 수라면 개수 증가
      cnt[num+1]+= 1;
    }
    else{ // 아니라면 9조각 내서 다시 세기
      for(int i=0; i<3; i++){
        for (int j=0; j<3; j++){
          cut(new int[]{start[0] + i*(n/3), start[1] + j*(n/3)}, n/3);
        }
      }
    }
  }
  
  public static void main(String[] args) throws Exception{
    BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(bf.readLine());

    N = Integer.parseInt(st.nextToken());
    matrix = new int[N][N];
    cnt = new int[3];
    
    for(int i=0; i<N; i++){
      st = new StringTokenizer(bf.readLine());
      for(int j=0; j<N; j++){
        matrix[i][j] = Integer.parseInt(st.nextToken());
      }
    }

    cut(new int[]{0,0}, N);

    for(int c:cnt) System.out.println(c);
  }
}