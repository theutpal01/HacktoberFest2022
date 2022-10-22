class ButterflyPattern {
    public static void main(String args[]){
        int n = 8;
        //Upper Half
        for(int i = 1; i <= n; i++){
            //left side
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }
            int spaces = 2*(n-i);
            for(int j = 1; j <= spaces; j++){
                System.out.print(" ");
            }
            //Right Side
            for (int j = 1; j <=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        // Lower Half      (Same as Upper Half ..just Reversed :)
        for(int i = n; i >= 1; i--){
            // lower left side
            for(int j = 1; j <= i; j++){
                System.out.print("*");
            }
            int spaces = 2*(n-i);
            for(int j = 1; j <= spaces; j++){
                System.out.print(" ");
            }
            // lower Right Side
            for (int j = 1; j <=i; j++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
