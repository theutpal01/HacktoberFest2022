import Java.util.*;   
import java.io.*;   
import java.util.Scanner;  
  
// create LCSExample1 class to find the Longest Common Subsequence  
class LCSExample1 {  
      
    // create findLengthOfLCS() method that returns the longest common sequences  
    public static String findLengthOfLCS(String str1, String str2, int p, int q) {  
      
        // create a matrix which act as a table for LCS  
        int[][] tableForLCS = new int[p + 1][q + 1];  
  
        // fill the table in the bottom up way  
        for (int i = 0; i <= p; i++) {  
            for (int j = 0; j <= q; j++) {  
                if (i == 0 || j == 0)  
                    tableForLCS[i][j] = 0;  // Fill each cell corresponding to first row and first column with 0  
                else if (str1.charAt(i - 1) == str2.charAt(j - 1))  
                    tableForLCS[i][j] = tableForLCS[i - 1][j - 1] + 1;  // add 1 in the cell of the previous row and column and fill the current cell with it   
                else  
                    tableForLCS[i][j] = Math.max(tableForLCS[i - 1][j], tableForLCS[i][j - 1]); //find the maximum value from the cell of the previous row and current column and the cell of the current row and previous column    
            }  
        }  
      
        int index = tableForLCS[p][q];  
        int temp = index;  
  
        char[] longestCommonSubsequence = new char[index + 1];  
        longestCommonSubsequence[index] = '\0';  
  
        int i = p, j = q;  
        String lcs ="";  
        while (i > 0 && j > 0) {  
            if (str1.charAt(i - 1) == str2.charAt(j - 1)) {  
                  
                longestCommonSubsequence[index - 1] = str1.charAt(i - 1);  
                i--;  
                j--;  
                index--;  
            }  
            else if (tableForLCS[i - 1][j] > tableForLCS[i][j - 1])  
                i--;  
            else  
                j--;  
        }  
          
        for (int k = 0; k <= temp; k++)  
            lcs = lcs + longestCommonSubsequence[k];  
              
        return lcs;  
    }  
    public static void main(String[] args) {  
          
        String str1, str2, LCS;  
          
        Scanner sc= new Scanner(System.in); //System.in is a standard input stream.  
        System.out.print("Enter first sequence: ");  
        str1 = sc.nextLine(); //reads string.  
          
        System.out.print("Enter second sequence: ");  
        str2 = sc.nextLine(); //reads string.  
          
        int p = str1.length();  
        int q = str2.length();  
          
        LCS = findLengthOfLCS(str1, str2, p, q);  
          
        System.out.print("Sequence1: " + str1 + "\nSequence2: " + str2);  
        System.out.println("\nLCS: "+LCS);  
          
    }  
}  
