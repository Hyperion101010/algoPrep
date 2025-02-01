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
    void op(ListNode* hd){
        ListNode* tmp = hd;
        while(tmp){
            cout<<tmp->val;
            tmp = hd->next;
        }
    }

    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* p1 = list1;
        ListNode* p2 = list2;

        ListNode* newlst = nullptr;
        ListNode* tmp_head = nullptr;

        // First we keep track of an old node as our newlst;
        // Now we keep 2 pointers p1 and p2, p1 is the list 1 and p2 is the list 2 pointer;
        // Now we check that the newlst pointer that we create will be pointed by which pointer;
        while(p1 && p2){

            // If p1 is greater than p2
            // Then is such scenario we need to set the newlst to p2 since p1 is greater than p2
            if(p1->val >= p2->val){

                // If our lst was already made, then we just change its next pointer
                // And advance the newlst to the next pointer where it pointed
                // p1 = 3, p2 = 2
                // This essentially means we are making the newlst next pointer point to 2 first
                // Then we also advance the newlst to now be at the position of 2
                if(newlst){
                    newlst->next = p2;
                    newlst = p2;
                }else{

                    // Scenario when we don't have a newlst
                    // In such case the newlst itself will point towards the smalles value pointer
                    // And now we also set our head that we are about to return.
                    newlst = p2;
                    tmp_head = newlst;
                }
                p2 = p2->next;
            }else{
                if(newlst){
                    newlst->next = p1;
                    newlst = p1;
                }else{
                    newlst = p1;
                    tmp_head = newlst;
                }
                p1 = p1->next;
            }
        }

        // After you are done with advancing both the pointer check if any leftover pointers are left
        // Take the leftover pointer and make the (old) newlst pointer take the remaining linkedlist
        if(p1 == nullptr && p2 == nullptr){
        }
        else if(!newlst){

            // Cases for when the newlst is new initialized, that means either p1 or p2 was nullptr
            if(p1){
                tmp_head = p1;
            }else{
                tmp_head = p2;
            }
        }
        else if(p1 == nullptr && newlst){

            // Adding the leftover pointers
            newlst->next = p2;
        }
        else if(p2 == nullptr && newlst){
            newlst->next = p1;
        }

        return tmp_head;
    }
};
