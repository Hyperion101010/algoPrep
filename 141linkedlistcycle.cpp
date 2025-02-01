/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* sp = head;
        ListNode* fp = head;

        // Checking the detectino of cycle using slow pointer and fast pointer method

        // Before advancing the slow and fast pointer we check if we really have a next pointer
        if(!sp || sp->next == nullptr){
            return false;
        }

        while(sp && fp){

            // Advance slow pointer and fast pointer by one position each.
            sp = sp->next;
            fp = fp->next;

            // Check if fp becomes null then it means we don't have a cycle.
            if(!fp){
                return false;
            }

            // Advance the fast pointer one more time.
            fp = fp->next;

            // After advancing the fast pointer now we check if fast pointer is again null
            // If it is null then it means that we don't have a cycle.
            if(!fp){
                return false;
            }

            // Now if the both pointers are equal that will mean that the fast and the slow pointer really matched.
            // Thus we now have a condition of cycle and then return true for this case.
            if(sp == fp){
                break;
            }
        }

        // Loop was detected so breaked and now we return true.
        return true;
    }
};
