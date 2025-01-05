class Solution {
public:
    int findLHS(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int ln = 0;
        for(int i =0; i< nums.size(); i++){
            int t = i;

            //traverse to next index where the numbers are different.
            while(t < nums.size() && nums[t] == nums[i]){
                t++;
            }
            if(t >= nums.size()){

                // case when the array is like [1, 2] and we have len answer as 2.
                if(nums[t-1] - nums[i] == 1){
                    ln = t-i;
                }
                continue;
            }
            else{
                if(nums[t] - nums[i] == 1){
                    while(t < nums.size() && nums[t] - nums[i] == 1){
                        t++;
                    }
                    int ln_new = t-i;
                    ln = max(ln, ln_new);
                }
            }
        }
        return ln;
    }
};
