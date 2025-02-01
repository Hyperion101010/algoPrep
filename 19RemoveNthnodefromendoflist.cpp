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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* sp = nullptr;
        ListNode* fp = nullptr;
        ListNode* prev = nullptr;
        ListNode* tmp = nullptr;

        int cnt = n;

        fp = head;
        sp = head;
        prev = nullptr;

        // The crux of the problem is we consider to start the problem with 2 pointers.
        // We start the traversal with a fast pointer that moves ahead in time and a slow pointer that moves only after n steps.
        // So that will mean when we exhaust the first n steps of the fast pointer, then we will reach at a point where slow pointer is a valid location
        // Cause in this scenario we will have sp at the valid location and thus we will be present at the correct location.
        while(sp){

            // If fp is exhausted that means we are the target location
            if(!fp){

                // If prev is null that means our pointer is at the head.
                if(!prev){
                    tmp = sp->next;
                    sp->next = nullptr;
                    head = tmp;
                }else{

                    // Case of when the pointer is at the correct location
                    // Just attach pointers and done.
                    prev->next = sp->next;
                }
                break;
            }

            // If the cnt is 0 now it means we will start updating the slow pointer to also meet with the location.
            if(cnt == 0){
                prev = sp;
                sp = sp->next;
                fp = fp->next;
            }
            else{

                // Only update the fast pointer till n steps are exhausted.
                fp = fp->next;
                cnt -=1;
            }
        }

        return head;
    }
};
