import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
       HashSet<String> set = new HashSet<>();
        for(String pb : phone_book){
            set.add(pb);
        }
       
        for(String pb : phone_book){
            for(int i=1; i<pb.length(); i++){
                if(set.contains(pb.substring(0, i))){
                    return false;
                }
            }
        }
        return true;
    }
}