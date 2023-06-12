class Solution {
    String[] pb;
    public boolean solution(String prefix) {
        for(int i = 0; i < pb.length; i++) {
            if(pb[i].equals(prefix)) continue;
            if(pb[i].startsWith(prefix)) {
                return false;
            }
        }
        return true;
    }
    public String findPrefix() {
        String prefix = pb[0];
        int minLen = prefix.length();
        for(int i = 1; i < pb.length; i++) {
            String cur = pb[i];
            if(cur.length() < minLen) {
                prefix = cur;
                minLen = cur.length();    
            }
        }
        return prefix;
    }
    public boolean solution(String[] phone_book) {
        pb = phone_book;
        String prefix = findPrefix();
        return solution(prefix);
    }
}
