/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    // Maintain a lookup map for visited nodes.
    // If you find that this node is visited don't call it.
    // If not visited then call it recursively.
    unordered_map<Node*, Node*> lkup;

    Node* cloneGraph(Node* node) {
        if(node == nullptr){
            return node;
        }
        if(lkup.find(node) != lkup.end()){
            return lkup[node];
        }

        // Maintain a map where you store a mapping of old node as key
        // And the value for the old node is the new copy of the node.
        // Now only copy it as the value.
        // You need to push back in its neighbors all copies you did by
        // recursively calling the clone method on all its neighbors.
        // This can be done using BFS also.

        Node* nw_node = new Node(node->val);
        lkup[node] = nw_node;

        for(auto itr: node->neighbors){
            Node* tmp_node = itr;
            Node* new_node_copy = cloneGraph(tmp_node);
            lkup[tmp_node] = new_node_copy;
            nw_node->neighbors.push_back(lkup[tmp_node]);
        }

        return lkup[node];
    }
};
