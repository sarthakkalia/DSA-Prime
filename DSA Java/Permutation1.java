import java.util.*;
public class Permutation1 {
    static void gen_perm(int ind,int[] arr, List<List<Integer>> ans){
        if(ind==arr.length){
            List<Integer> ds =new ArrayList<>();
            for(int i=0;i<arr.length;i++){
                ds.add(arr[i]);
            }
            ans.add(new ArrayList<>(ds));
            return;
        }
        for(int i=ind;i<arr.length;i++){
            swap(i,ind,arr);
            gen_perm(ind+1,arr,ans);
            swap(i,ind,arr);
        }
    }
    static void swap(int i,int ind,int[] arr){
        int temp=arr[i];
        arr[i]=arr[ind];
        arr[ind]=temp;
    }
    public List<List<Integer>> permute(int[] arr){
        List<List<Integer>> ans=new ArrayList<>();
        gen_perm(0,arr,ans);
        return ans;
    }
    public static void main(String[] args) {
        int[] arr={1,2,3};
        Permutation1 obj=new Permutation1();
        List<List<Integer>> perm =obj.permute(arr);
        for(List<Integer> e: perm){
            System.out.println(e);
        }
        
    }
}
