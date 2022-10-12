import java.util.Scanner;
class Main {
  public static String alphabet="abcdefghijklmnopqrstuvwxyz";
  public static String encrpyt(String s,int key){
    s=s.toLowerCase();
    String ciphertext="";
    for(int i=0;i<s.length();i++){
      int shift=alphabet.indexOf(s.charAt(i));
      int newalpha=(shift+key)%26;
      char ch=alphabet.charAt(newalpha);
      ciphertext+=ch;
    }
    return ciphertext;
  }
  public static String decrypt(String s,int key){
    s=s.toLowerCase();
    String plaintext="";
    for(int i=0;i<s.length();i++){
      int pos=alphabet.indexOf(s.charAt(i));
      int newval=(pos-key)%26;
      if(newval<0){
        newval=alphabet.length()+newval;
      }
      char rep=alphabet.charAt(newval);
      plaintext+=rep;
    }
    return plaintext;
  }
  public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    System.out.println("enter the text");
    String s=sc.next();
    System.out.println("enter the key");
    int key=sc.nextInt();
    String cipher=encrpyt(s,key);
    System.out.println("cipher text:-"+cipher);
    String plain =decrypt(cipher, key);
    System.out.println("plain text :-"+plain);
      }
}
