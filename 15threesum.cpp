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
        for(fst =0; fst<nums.size() - 2; fst++){
            if(fst > 0 && nums[fst] == nums[fst-1]){
                continue;
            }
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

// Ans 2 with solution

class Solution {
public:

    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> ans;
        vector<vector<int>> ans2;
        sort(nums.begin(), nums.end());
        for(int i =0; i<nums.size() - 2;i++){

            // skip checking those iteration where we have the same "i" th element for the array.
            // since we want duplicate triples it means we will end up with the same set.
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            int fst = i + 1;
            int snd = nums.size() - 1;
            while(fst < nums.size() - 1 && snd > fst){
                int target = nums[i] + nums[fst] + nums[snd];
                if (target == 0){
                    vector<int> tmp;
                    tmp.push_back(nums[i]);
                    tmp.push_back(nums[fst]);
                    tmp.push_back(nums[snd]);
                    ans.insert(tmp);
                    fst+=1;
                    continue;
                }else if(target > 0){
                    // the only way we can decrease the count total is if we move the last pointer
                    // towards the left side since that is the only pointer that can decrease the addition
                    snd-=1;
                }else{
                    // the only way we can increase the count total is if we move the first pointer
                    // towards the right side since that is the only pointer that can increase the addition
                    fst+=1;
                }
            }
        }
        for(auto itr = ans.begin(); itr != ans.end(); itr ++){
            ans2.push_back(*itr);
        }
        return ans2;
    }
};
