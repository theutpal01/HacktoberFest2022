public class SearchStrings{
    public static void main(String[] args){
        System.out.println("This is a program to check whether a character is present in a String or not.");
        System.out.println();
        String name = "Biswa";
        char target ='i';
        System.out.println(presentOrNot(name,target));

        }
        static boolean presentOrNot(String string_value, char target_value) {
            if (string_value.length()==0){
                return false;
            }
            for(int i=0;i<string_value.length();i++){
                if(target_value==string_value.charAt(i)){
                    return true;
                }
            }
            return false;
    }
}