import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSumOptimal {
    public static List<List<Integer>> threeSum(int[] arr){
        List<List<Integer>> ans= new ArrayList<>();
        Arrays.sort(arr);
        int n=arr.length;
        for(int i=0;i<n;i++){
            
            if (i != 0 && arr[i] == arr[i - 1]) continue;  //remove duplicates:

            int j=i+1; int k=n-1;
            while (j<k) {
                int sum=arr[i]+arr[j]+arr[k];
                if(sum < 0){
                    j++;
                }
                else if(sum > 0 ){
                    k--;
                }
                else{
                    List<Integer> temp = Arrays.asList(arr[i],arr[j],arr[k]);
                    ans.add(temp);
                    j++; k--;

                    //skip the duplicates:
                    while (j < k && arr[j] == arr[j - 1]) j++;
                    while (j < k && arr[k] == arr[k + 1]) k--;
                }

            }

        }
        return ans;
    }
    public static void main(String[] args) {
        int[] arr = { -1, 0, 1, 2, -1, -4};
        List<List<Integer>> ans= threeSum(arr);
        // for(List<Integer> it : ans){
        //     System.out.print(it);
        // }
        System.out.println(ans);
    }
}
