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

    // The logic for checking if a tree is a BST is if you generate a inorder traversal of the tree.
    // Then the inorder traversal of the tree should actually be a sorted array.
    // This makes sure each node in left subtree is always counted first and it is is then checked if less than the root.
    // Thus we don't need to check for the right subtree since its handled in the inorder traversal.
    // Thus we check if a tree is a BST.
    void inorder(TreeNode* root){
        if(root == nullptr){
            return;
        }

        inorder(root->left);

        tmp.push_back(root->val);

        inorder(root->right);

        return;
    }

    bool isValidBST(TreeNode* root) {
        inorder(root);

        for(int i=0; i < tmp.size() - 1; i++){
            if(tmp[i] >= tmp[i+1]){
                return false;
            }
        }
        return true;
    }
};
