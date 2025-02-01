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
    TreeNode* invertTree(TreeNode* root) {

        // You start with root of the node
        // Then you are traversing and this is the base condition to stop if your root reached is nullptr.
        if(!root){
            return root;
        }

        // As an inversion operation, we are going to swap the nodes of the tree.
        TreeNode* tmp = nullptr;
        tmp = root->left;
        root->left = root->right;
        root->right = tmp;

        // Invert the left and right sub trees.
        TreeNode* lft = invertTree(root->left);
        TreeNode* rgt = invertTree(root->right);

        // Return the root which will have the inverted tree nodes.
        return root;
    }
};
