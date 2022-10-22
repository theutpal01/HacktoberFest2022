import java.util.Scanner;

public class fact {
    public static void main(String[] args) {
        System.out.println("Enter the number for factorial");
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();
        int fact = 1;
        int i = 1;
        while( i <=num){

            fact = fact*i;
            
            i++;
            
        }
        System.out.println(fact);
        in.close();
    }
}
