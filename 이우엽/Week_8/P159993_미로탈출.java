import java.util.*;
class P159993_미로탈출 {
    char[][] gMaps;
    int cnt;
    int[] dx = {-1, 0, 1, 0};
    int[] dy = {0, 1, 0, -1};
    int flag = 0;
    
    public void calExitDist(int[] start) {
        int row = gMaps.length;
        int col = gMaps[0].length;
        
        boolean[][] isVisited = new boolean[row][col];
        
        Queue<int[]> queue = new ArrayDeque<>();
        isVisited[start[0]][start[1]] = true;
        queue.offer(start);
        
        while(!queue.isEmpty()) {
            int len = queue.size();
            for(int t = 0; t < len; t++) {
                int[] cur = queue.remove();
                int x = cur[0];
                int y = cur[1];
                // System.out.println("x: " + x + " y: " + y);
                for(int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || ny < 0 || nx >= row || ny >= col) continue;
                    if(isVisited[nx][ny]) continue;
                    if(gMaps[nx][ny] == 'O') {
                        isVisited[nx][ny] = true;
                        queue.offer(new int[]{nx, ny});
                        // System.out.println("nx: " + nx + " ny: " + ny);
                    } else if(gMaps[nx][ny] == 'X') {
                        continue;
                    } else if(gMaps[nx][ny] == 'E') {
                        flag = 1;
                        cnt++;
                        return;
                    }
                }
            }
            cnt++;
        }
        
        return;
    }
    public int[] calLeverDist(int[] start) {
        int row = gMaps.length;
        int col = gMaps[0].length;
        
        boolean[][] isVisited = new boolean[row][col];
        
        Queue<int[]> queue = new ArrayDeque<>();
        isVisited[start[0]][start[1]] = true;
        queue.offer(start);
        
        while(!queue.isEmpty()) {
            int len = queue.size();
            for(int t = 0; t < len; t++) {
                int[] cur = queue.remove();
                int x = cur[0];
                int y = cur[1];
                for(int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    if(nx < 0 || ny < 0 || nx >= row || ny >= col) continue;
                    if(isVisited[nx][ny]) continue;
                    if(gMaps[nx][ny] == 'O' || gMaps[nx][ny] == 'E') {
                        isVisited[nx][ny] = true;
                        queue.offer(new int[]{nx, ny});
                    } else if(gMaps[nx][ny] == 'X') {
                        continue;
                    } else if(gMaps[nx][ny] == 'L') {
                        cnt++;
                        // System.out.println("nx: " + nx + " ny: " + ny);
                        return new int[]{nx, ny};
                    }
                }
            }
            cnt++;
            // break;
        }
        // System.out.println("cnt: " + cnt);
        return new int[]{-1, -1};
    }
   
    public int[] findStart(String[] maps) {
        int i = 0;
        for(String row : maps) {
            char[] rowArr = row.toCharArray();
            // System.out.println(Arrays.toString(rowArr));
            for(int j = 0; j < rowArr.length; j++) {
                if(rowArr[j] == 'S') { 
                    return new int[]{i, j};
                }
            }
            i++;
        }
        return new int[]{};
    }
    public int solution(String[] maps) {
        int answer = 0;
        gMaps = new char[maps.length][maps[0].length()];
        for(int i = 0; i < maps.length; i++) {
            for(int j = 0; j < maps[0].length(); j++) {
                gMaps[i][j] = maps[i].charAt(j);
            }
        }
        for(int i = 0; i < gMaps.length; i++) {
            System.out.println(Arrays.toString(gMaps[i]));
        }   
        
        int[] start = findStart(maps);
        System.out.println(Arrays.toString(start));

        int[] cur = calLeverDist(start);
        if(cur[0] == -1) return -1;
        calExitDist(cur);
        if(flag == 0) return -1;
        System.out.println("shortest: " + cnt);
        return cnt;
    }
}