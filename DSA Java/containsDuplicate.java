import java.util.HashSet;
import java.util.Set;

public class containsDuplicate {
    public static boolean contDup(int[] arr){
        Set<Integer> set=new HashSet<>();
        for(int i=0;i<arr.length;i++){
            if(set.contains(arr[i])){
                return true;
            }
            else{
                set.add(arr[i]);
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int[] arr={1,2,3,1};
        System.out.println(contDup(arr));
    }
}
