"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        """
            The crux of the problem is maintaining two lookup tables.
            In first interation we keep an index lookup 
            where for each pointer of the list we keep mapping of that random pointer as key to the index.
            And another where for the index we keep the mapping to store the new node.

            Then in second interation we just resolve it again and return back.
        """
        
        new_list_head = Node(0)
        head_pointer = new_list_head

        temp_head = head

        lkup_by_idx = {}
        lkup_by_new_idx = {}
        idx = 0

        while temp_head is not None:
            # Make a new node
            temp_node = Node(temp_head.val)

            # Assign this new node to the new list
            new_list_head.next = temp_node

            # Store the random pointer at the current length
            lkup_by_idx[temp_head] = idx

            lkup_by_new_idx[idx] = temp_node

            # Move the head pointer ahead.
            temp_head = temp_head.next

            # Move our new list pointer to keep copying.
            new_list_head = temp_node

            idx += 1
        
        temp_head = head
        new_list_head = head_pointer.next
        idx = 0

        while temp_head is not None:
            random_head_ptr = temp_head.random

            if random_head_ptr is None:
                new_list_head.random = None
            else:
                hd_key = lkup_by_idx[random_head_ptr]

                # Get new node which is at the position for this node
                new_list_head.random = lkup_by_new_idx[hd_key]

            new_list_head = new_list_head.next
            temp_head = temp_head.next
        
        return head_pointer.next
