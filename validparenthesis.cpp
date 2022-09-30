class Solution {
public:
    int longestValidParentheses(string s) {
       int ans=0,len=0;
    stack<int> st;
    st.push(-1);
    for(int i=0; i<s.size(); i++){
        if(s[i]==')'){
            st.pop();
            if(st.empty()) st.push(i);
            else len=i-st.top();
        }
        else st.push(i);
        ans=max(ans, len);
    }
    return ans;
    }
};
