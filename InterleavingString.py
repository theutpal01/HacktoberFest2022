class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1)+len(s2):
            return False
        # state: dp[i][j] denote whether the first i+j letters in s3 is a 
        # interleaving of the first i elements in s1 and the first j
        # elements in s2
        n, m = len(s1), len(s2)
        dp = [[False]*(m+1) for _ in range(n+1)]
        
        # initialization: fill in the first row and column
        dp[0][0] = True
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, m+1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        
        # state transition: matching last character in s1 and s2 with that
        # of s3
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s3[i+j-1]:         # s3[:3] = "abc", s1[2] = 'c'
                    dp[i][j] = dp[i-1][j]
                if s2[j-1] == s3[i+j-1]:         # s3[:3] = "abc", s2[2] = 'c'
                    dp[i][j] = dp[i][j] or dp[i][j-1]
            
        # result: whether entire s3 is an interleaving of entire s1 and s2
        return dp[-1][-1]
