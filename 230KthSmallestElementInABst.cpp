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
    vector<int> tmp;

    // The logic is same as checking if a tree is BST.
    // First run a inorder traversal to have an array of values in an increasing order.
    // Then finally keeping iterating through the lowest values and check when k is 0 then return the answer.
    void inorder(TreeNode* root){
        if(root == nullptr){
            return;
        }

        inorder(root->left);

        tmp.push_back(root->val);

        inorder(root->right);

        return;
    }

    int kthSmallest(TreeNode* root, int k) {
        inorder(root);

        for(int i=0; i < tmp.size(); i++){
            k-=1;
            if(k==0){
                return tmp[i];
            }
        }
        return 0;
    }
};
