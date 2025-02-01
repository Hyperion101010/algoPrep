/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    void reorderList(ListNode* head) {

        // In this problem I am using deque as my stack
        // So first I'll traverse the linkedlist to store my elemtns in a reverse order
        // As it would happen in a stack
        deque<ListNode*> dq;

        ListNode* sp = head;
        ListNode* fp = nullptr;
        ListNode* newlst = nullptr;
        ListNode* tmp = nullptr;

        // Traversal to store nodes in a deque.
        while(sp){
            dq.push_back(sp);
            sp = sp->next;
        }

        int ln = dq.size();
        int cnt = 0;

        sp = head;

        // Keep running the loop until we have our length match up to the midpoint
        while(cnt < (int) (ln/2)){

            // Add initial cases when the list item has no element then it's always the head.
            if(!newlst){
                newlst = sp;
            }else{

                // If the head is present then append the prev to current head and advance.
                newlst->next = sp;
                newlst = sp;
            }

            // Advance head for the next loop.
            sp = sp->next;

            // Pop things back from the queue so that they are fetched in the reverse order.
            ListNode* tt = dq.back();
            dq.pop_back();

            // Append the poped element from the stack (deque) in our list and advance.
            newlst->next = tt;
            newlst = tt;
            cnt +=1;
        }

        // If cnt is 0 that means we have an empty linkedlist supplied.
        if(cnt == 0){
            return;
        }

        // If the linkedlist length is odd that means that we have append the middle element
        // This will ofcourse be present in the deque (stack).
        if(ln % 2 == 1){

            // Take the element from deque (stack), append it and advance
            ListNode* ttmp = dq.back();
            dq.pop_back();
            newlst->next = ttmp;
            newlst = ttmp;
        }

        // Set the next pointer as null to terminate our new linedlist.
        newlst->next = nullptr;
    }
};
