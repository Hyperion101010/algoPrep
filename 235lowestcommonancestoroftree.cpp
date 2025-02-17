/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr){
            return root;
        }

        // In our solution, we need to consider 3 conditions
        // Since this is a binary tree.
        // When both p and q are greater than the root value.
        // In this scenario they will lie in the right sub tree.
        // When both p and q are less than the root value.
        // In this scenario theu will lie in the left sub tree
        // Lies in the right sub tree.
        // If we can't find it being in left or right sub tree then its either the root itself.
        // This is because the root will have p and q either on left and right cases.
        // There can also be a case when either p or q equal to root, that means we have met the end criteria for our node.
        if(p->val > root->val && q->val > root->val){
            return lowestCommonAncestor(root->right, p, q);
        }
        if(p->val < root->val && q->val < root->val){
            return lowestCommonAncestor(root->left, p, q);
        }

        return root;

        //int mn = min(p->val, q->val);
        //int mx = max(p->val, q->val);

        /*
        Other end criteria's that I considered but in all cases we return only root, so just return root.

        if(mn < root->val && mx < root->val){
            return root;
        }
        if(mn == root->val){
            return root;
        }
        return root;
        */
    }
};
