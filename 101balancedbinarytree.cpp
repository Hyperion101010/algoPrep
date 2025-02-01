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
    int dpth(TreeNode* root){
        if(!root){
            return 0;
        }
        int lfdepth = 1 + dpth(root->left);
        int rgtdepth = 1 + dpth(root->right);
        return max(lfdepth, rgtdepth);
    }

    bool isBalanced(TreeNode* root) {
        if(!root){
            return true;
        }

        // The solution of the problem is to search in left and right subtrees
        // Try to find the depth of both ends left and right and then return true or false based on whether it is more than depth 1 or not
        // Similarly check for left and right substrees if they are balanced.
        int lftree = dpth(root->left);
        int rgttree = dpth(root->right);

        if(abs(lftree - rgttree) > 1){
            return false;
        }
        return isBalanced(root->left) && isBalanced(root->right);
    }
};
