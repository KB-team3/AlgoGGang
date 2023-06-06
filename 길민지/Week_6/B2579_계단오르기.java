import java.io.*;
import java.util.*;

class Main {
  static int N;
  static int score[];
  static int max = 0;
  static int dp[][]; // [현재 층], [이전에 몇칸 올랐는지] 0 - 1층 / 1 - 2층

  public static void main(String[] args) {
    // 입력 및 초기화
    Scanner sc = new Scanner(System.in);
    N = sc.nextInt();
    score = new int[N + 1];
    dp = new int[N + 1][2];
    for (int i = 1; i < N + 1; i++) {
      score[i] = sc.nextInt();
    }

    // 계단이 1개인 경우
    if(N==1) {
      System.out.println(score[1]);
      return;
    }

    // 1층 세팅
    dp[1][0] = score[1];
    dp[1][1] = score[1];

    for (int i = 2; i < N + 1; i++) {
      // 1층 아래에서 올라온 경우
      dp[i][0] = Math.max(dp[i][0], dp[i - 1][1] + score[i]);

      // 2층 아래에서 올라온 경우
      int m = Math.max(dp[i - 2][0] + score[i], dp[i - 2][1] + score[i]);
      dp[i][1] = Math.max(dp[i][1], m);
    }

    System.out.println(Math.max(dp[N][0], dp[N][1]));

  }
}