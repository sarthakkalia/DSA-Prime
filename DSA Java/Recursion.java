class Recursion{
    static int count=1;
    public static void print(){
        if (count>3){
            return;
        }
        System.out.println(count);
        count+=1;
        print();
    }
    public static void main(String[] args) {
        print();
    }
}