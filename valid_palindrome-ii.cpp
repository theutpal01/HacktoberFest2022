class Solution {
public:
    
    bool isPalindrome(string s,int start,int end){
        
        while(start<end){
            if(s[start]!=s[end]) return false;
            start++;
            end--;
        }
        return true;
    }
    
    bool validPalindrome(string s) {
        int i = 0,j = s.length() - 1;
        while(i<j){
             if(s[i]!=s[j]){
                 return isPalindrome(s,i+1,j) || isPalindrome(s,i,j - 1);
             }
            i++,j--;
        }
        return true;
    }
};
