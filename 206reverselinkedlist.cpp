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


// How to do it?
// First have 2 pointers 
// 1. prev and 2. curr
// First make prev ---> nullptr
// Second curr ---> head
// Save curr->next somewhere in the tmp variable
// Set curr->next = prev
// Set prev = curr
// Set curr = tmp i.e curr = curr->next
// Eg: We have pointers, 1 -> 2 -> 3 -> 4
// We store prev as nullptr
// We store curr as 1
// We store tmp as curr->next as 2
// We set curr->next as prev i.e 1 -->nullptr
// prev = curr, prev = 1
// curr = curr->next i.e curr = 2
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* tmp = nullptr;

        while(curr != nullptr){
            tmp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = tmp;
        }
        
        return prev;
    }
};
