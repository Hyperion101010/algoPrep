class Solution {
public:
    int ln(string s){
        return s.length();
    }
    
    string mx(string a, string b){
        return ln(a)>ln(b)?a:b;
    }
    
    string calPal(string s, int l, int r, int sz){
        while(l>=0 && r<sz && s[l]==s[r]){
            l--;
            r++;
        }
        string x = s.substr(l+1, r-l-1);
        return x;
    }
    
    
    string longestPalindrome(string s) {
        int sz = s.length();
        string tmp;
        if(sz==0){
            return 0;
        }
        for(int i=0;i<sz;i++){
            string ev = calPal(s,i,i,sz);
            string od = calPal(s,i,i+1,sz);
            tmp = mx(tmp,ev);
            tmp = mx(tmp, od);
        }
        return tmp;
    }
};
