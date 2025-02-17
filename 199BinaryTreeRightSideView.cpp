/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        TreeNode* tmp;
        deque<TreeNode*> q;

        vector<int> res;

        if(root != nullptr){
            q.push_back(root);
        }

        // The implementation is as simple as a Level Order Traversal with only storing the last entries in array for the right hand side view.
        // Thus run the Level Order Traversal.
        // And finally insert the elements in the result array after each for loop.
        while(!q.empty()){
            vector<TreeNode*> tmp_vals;
            vector<int> ans;

            for(auto itr = q.begin(); itr != q.end(); itr++){
                tmp = *itr;

                ans.push_back(tmp->val);

                if(tmp != nullptr){
                    if(tmp->left != nullptr){
                        tmp_vals.push_back(tmp->left);
                    }
                    if(tmp->right != nullptr){
                        tmp_vals.push_back(tmp->right);
                    }
                }

                q.pop_front();
            }

            res.push_back(ans[ans.size()-1]);
            ans.clear();
            
            for(auto itr = tmp_vals.begin(); itr != tmp_vals.end(); itr++){
                q.push_back(*itr);
            }

        }

        return res;
    }
};
