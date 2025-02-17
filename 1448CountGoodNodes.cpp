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

    // The main idea of the concept is to count good nodes.
    // A good node is possible when the max value from the root is less than the current nodes value.
    // We can write a recursive program that checks and computes the count of good nodes based on a condition.
    int traverse(TreeNode* root, int mx_val){

        // Base conditon to return a 0 count.
        if(root == nullptr){
            return 0;
        }

        // When the current node val is greater than max val that means we found a good node.
        // Now add 1 count in our traversal and return.
        // Split the operation on the two halves and then return the result.
        if(root->val >= mx_val){
            return 1 + traverse(root->left, root->val) + traverse(root->right, root->val);
        }

        // If not found in current node, keep recursively checking in two halves.
        return traverse(root->left, mx_val) + traverse(root->right, mx_val);
    }

    int goodNodes(TreeNode* root) {
        return traverse(root, -100000000000);
    }
};
