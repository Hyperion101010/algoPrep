// Look how we used the the set insert here.

class Solution {
public:

    int bin_search(int ofst, int target, vector<int> nums){
        int lft = ofst;
        int rgt = nums.size() - 1;
        //cout<<ofst<<" "<<target;
        if (ofst > nums.size() - 1){
            return -1;
        }
        while(lft <= rgt){
            int md = (lft + rgt)/2;
            if(nums[md] == target){
                return md;
            }else if(nums[md] > target){
                rgt = md - 1;
            }else{
                lft = md + 1;
            }
        }
        return -1;
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        int fst = 0, snd = 0;
        set<vector<int>> ans;
        vector<vector<int>> ans2;
        unordered_map<int, bool> lkup;
        sort(nums.begin(), nums.end());
        for(fst =0; fst<nums.size() ; fst++){
            snd = fst + 1;
            while(snd < nums.size() - 1){
                int target = (-1)*( nums[fst] + nums[snd]);
                if(bin_search(snd + 1, target, nums) > 0){
                    //cout<<"found "<<target;
                    vector<int> tmp;
                    //tmp.push_back(nums[fst]);
                    //tmp.push_back(nums[snd]);
                    //tmp.push_back(target);
                    ans.insert({nums[fst], nums[snd], target});
                }
                snd += 1;
            }
        }
        for(auto itr = ans.begin(); itr != ans.end(); itr ++){
            ans2.push_back(*itr);
        }
        return ans2;
    }
};
