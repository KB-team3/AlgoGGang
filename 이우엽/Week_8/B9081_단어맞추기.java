import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.TreeSet;

public class B9081_단어맞추기 {
	static int N;
	static String[] words;
	static TreeSet[] tree;
	public static void insertTree(int idx, String word) {
		for(int i = 0; i < word.length(); i++) {
			char cur = word.charAt(i);
			tree[idx].add(cur);
		}
	}
	public static void init() throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		tree = new TreeSet[N];
		words = new String[N];
		for(int i = 0; i < N; i++) {
			words[i] = br.readLine();
		}
		
		for(int i = 0; i < N; i++) {
			tree[i] = new TreeSet();
		}
	}
	public static void main(String[] args) throws NumberFormatException, IOException {
		init();
		System.out.println(Arrays.toString(words));
		System.out.println(words[0].charAt(0) - '0');
		//solution
		//insert tree
		for(int i = 0; i < N; i++) {
			insertTree(i, words[i]);
			System.out.println(tree[i]);
		}
	}
}
