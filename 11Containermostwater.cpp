class Solution {
public:
    int max(int a, int b){
        return a>b?a:b;
    }
    
    int area(int b1, int b2, int ds1, int ds2){
        if(b1> b2){
            return abs(ds1-ds2)*b2;
        }
        return abs(ds1-ds2)*b1;
    }
    
    int maxArea(vector<int>& height) {
        int lf = 0;
        int rg = height.size()-1;
        int mx = 0;
        while(lf < rg){
            int ar1 = area(height[lf], height[rg], lf, rg);
            mx = max(mx, ar1);
            if(height[lf] > height[rg]){
                rg--;
            }
            else{
                lf++;
            }
        }
        return mx;
    }
};
