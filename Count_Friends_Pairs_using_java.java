import java.io.*;
import java.util.*;

class Solution {
  int mod = (int)1e9 + 7
  public long countFriendsPairings(int n, long[] dp) {
    if (n == 0) {
      return dp[n] = 1;
    }

    if (dp[n] != -1) {
      return dp[n];
    }
    // either we can remain single or we can make pairs 
    // multiplying by (n-1) cause we have n-1 call 
    /*
      5 
        -> 4 (when 1 will remain single) 
        -> 3 * (5 - 1) (when 1 will want to form pair with 2 , 3 , 4 , 5 so instead of making multiple calls we can just multiply with n-1)
    */
    long single = countFriendsPairings(n - 1, dp);
    long pair = n - 2 >= 0 ? countFriendsPairings(n - 2, dp) * (n-1) : 0;

    return dp[n] = (single + pair % mod) % mod;
  }
  
  public long countFriendsPairings(int n) {
    long[] dp = new long[n+1];
    Arrays.fill(dp,-1);
    return countFriendsPairings(n,dp);
  }
}
