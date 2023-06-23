import java.util.*;
class Solution {
    public int[] di = {0,0,1,-1};
    public int[] dj = {1,-1,0,0};
    public boolean[][] isVisited;
    
    // 통로 체크
    public boolean chkValid(String[] maps, int i, int j){
        if (i<0||j<0||i>=maps.length||j>=maps[0].length()||maps[i].charAt(j)=='X') return false;
        return true;
    }
            
    public int BFS(String[] maps, int si, int sj, char target){
        Queue<Integer[]> que = new ArrayDeque<>();
        que.add(new Integer[]{si, sj, 0}); // i좌표, j좌표, 이동시간
        
        isVisited = new boolean[maps.length][maps[0].length()];
        isVisited[si][sj]=true;
        
        while(!que.isEmpty()){
            Integer[] now = que.poll();
            // 4방탐색
            for(int i=0; i<4; i++){
                int ni = now[0]+di[i];
                int nj = now[1]+dj[i];
                int nd = now[2]+1;
                
                if (!chkValid(maps, ni, nj)||isVisited[ni][nj]) continue;
                if (maps[ni].charAt(nj)==target) return nd;
                que.add(new Integer[]{ni, nj, nd});
                isVisited[ni][nj] = true;
            }
        }
        return -1;
    }
    
    public int solution(String[] maps) {
        // 각 지점 위치 찾기
        int[] start = new int[2];
        int[] lever = new int[2];
        int[] end = new int[2];
        for(int i=0; i<maps.length; i++){
            String line = maps[i];
            for(int j=0; j<maps[i].length(); j++){
                if(line.charAt(j)=='S') start = new int[]{i, j};
                else if (line.charAt(j)=='L') lever = new int[]{i, j};
                else if(line.charAt(j)=='E') end = new int[]{i, j};
            }
        }
        
        // 시작점->레버 찾기
        int l = BFS(maps, start[0], start[1], 'L');
        if (l == -1) return -1;
        
        // 레버->출구 찾기
        int e = BFS(maps, lever[0], lever[1], 'E');
        if (e == -1) return -1;
        
        return l+e;
    }
}