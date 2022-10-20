import java.util.*;
class reverse
{
  public static void main(String[]args)
  {
    Scanner sc=new Scanner(System.in);
    System.out.println("Enter a string");
    String s=sc.nextLine();
    System.out.println("Input taken:"+s);
    System.out.print("Reverse String:");
    for(int i=s.length()-1;i>=0;i--)
      System.out.print(s.charAt(i));
  }
}
