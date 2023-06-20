import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class B9081_단어맞추기 {
    static int N;
    static String input[];
    public static void init(){
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.nextLine());

        input = new String[N];
        for(int i=0; i<N; i++){
            input[i] = sc.nextLine();
        }
    }
    public static void solution(){
        for(String s:input){
            boolean isLast = true;
            char[] word = s.toCharArray();

            int now = word.length-1;
            for(int i=word.length-2; i>=0; i--){ // 뒤에서부터 체크
                if(word[i]<word[now]){ // 감소 시
                    isLast = false;
                    char temp = word[i];
                    for(int j=word.length-1; j>i; j--){
                        if(word[j]>temp){ // 바꿀 단어보다 더 큰 단어 나오면 교체
                            word[i] = word[j];
                            word[j] = temp;
                            break;
                        }
                    }
                    Arrays.sort(word, i+1, word.length); // 뒷부분 정렬
                    System.out.println(new String(word)); // 출력
                    break;
                } else {
                    now = i;
                }
            }
            if(isLast) System.out.println(s); // 마지막 단어인 경우
        }
    }

    public static void main(String args[]){
        init();
        solution();
    }
}
