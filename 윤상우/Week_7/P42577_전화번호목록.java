package temp;

import java.util.HashSet;
import java.util.Set;

public class P42577_전화번호목록 {
    public boolean solution(String[] phone_book) {

        Set<String> set = new HashSet<String>();

        for(String phone : phone_book){
            set.add(phone);
        }

        for(String phone : phone_book){
            for(int i=1; i<phone.length(); i++){
                if(set.contains(phone.substring(0,i))){
                    return false;
                }
            }
        }


        return true;
    }
}
