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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> tmp;
        deque<TreeNode*> q;

        // The logic of this problem is actually each level of tree will be the entire thing present in the queue.
        // So, first we start with queue as empty.
        // We put the root inside the queue
        // After that we start our while loop.
        // In each while loop step we first extract all the queue elements that we have.
        // For each queue present in that iteration will actually be the same level of the tree.
        // So we store them and also insert the next level data in some temp variable to insert into the queue at last.
        // Then after the for loop we put all the new elements in the queue and then again run the while loop.
        // in this manner the Inorder traversals is to move from left to right for each level and store values in array and return them.

        // Check if root is null.
        if(root != nullptr){
            q.push_back(root);
        }

        // Run the queue
        while(!q.empty()){
            
            TreeNode* ptr = q.front();
            vector<int> ans;
            vector<TreeNode*> tmp_tree;

            // Iterate through the queue each element, this will be the same level values so we will store them somewhere.
            // Also we will store their left and right childs which should be in queue for the next level.
            for(auto itr = q.begin(); itr != q.end() ; itr++){
                TreeNode* ptr = *itr;

                // queue element shouldn't be null
                if(ptr != nullptr){
                    if(ptr->left != nullptr){

                        // We push elements that are left child for next iteration.
                        tmp_tree.push_back(ptr->left);
                    }
                    if(ptr->right != nullptr){
                        // We push elements that are right child for next iteration.
                        tmp_tree.push_back(ptr->right);
                    }

                    // This is result for our current level.
                    ans.push_back(ptr->val);
                }
                q.pop_front();
            }

            // Store answer
            tmp.push_back(ans);

            for(auto itr2 = tmp_tree.begin(); itr2 != tmp_tree.end(); itr2++){

                // Store the current left and right child nodes in queue for driving next iteration.
                q.push_back(*itr2);
            }
        }

        // Return the final answer back to system.
        return tmp;
    }
};
