// Print Name N times using Recursion
public class Recursion1 {
    static void fun(int i,int n){
        if (i>n){
            return;
        }
        System.out.println("Sarthak");
        fun(i+1,n);
    }
    public static void main(String[] args) {
        fun(1,4);
    }
}
