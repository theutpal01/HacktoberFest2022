// 1. Input n, representing the count of items.
// 2. Input n numbers, representing the values of n items.
// 3. Input another n numbers, representing the weights of n items.
// 3. Input "cap", which is the capacity of a bag you have.
// 4. Calculate and print the maximum value that can be created in the bag without overflowing it's capacity.
// Note -> Each item can be taken 0 or 1 number of times. You are not allowed to put the same items again.

package HacktoberFest2022;
import java.util.*;
public class ZeroOneKnapSack{
    public static void main(String[] args){
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        
        int[] value = new int[n];
        for(int i=0; i<n; i++){
            value[i] = scn.nextInt();
        }
        
        int[] weight = new int[n];
        for(int i=0; i<n; i++){
            weight[i] = scn.nextInt();
        }
        
        int cap = scn.nextInt();
        
        int[][] dp = new int[n+1][cap+1];
        for(int i=1; i<dp.length; i++){
            for(int j=1; j<dp[0].length; j++){
                if (j >= weight[i-1]){
                    int remCap = j - weight[i-1];
                    
                    int play = value[i-1] + dp[i-1][remCap];
                    int notPlay = dp[i-1][j];
                    
                    if(play > notPlay) dp[i][j] = play;
                    else dp[i][j] = notPlay;
                }
                else dp[i][j] = dp[i-1][j];
            }
        }
        System.out.println(dp[n][cap]);
        scn.close();
    }
}