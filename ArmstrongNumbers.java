public class ArmstrongNumbers {
    public static void main(String[] args) {
        System.out.println(armNum(153));
    }
    static boolean armNum(int n){
    int original = n;
    int n4=0;

    while(n>0){
    int n2=n%10;
    n=n/10;    
    n4=n4+n2*n2*n2;
    }
    return n4==original;
}
}
