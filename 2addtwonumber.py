# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        l1_ptr = l1
        l2_ptr = l2

        """
            The algorithm is plainly simple.
            Iterate till you have a carry of a value from either pointer.
            Then return the head of the linked list.
        """

        temp_start = None
        start_node = None
        prev = None

        while l1_ptr is not None or l2_ptr is not None or carry > 0:

            if l1_ptr is None:
                l1_val = 0
            else:
                l1_val = l1_ptr.val
            
            if l2_ptr is None:
                l2_val = 0
            else:
                l2_val = l2_ptr.val

            temp_val = l1_val + l2_val + carry
            
            carry = temp_val // 10
            temp_val = temp_val % 10

            start_node = ListNode(temp_val)

            if l1_ptr:
                l1_ptr = l1_ptr.next
            
            if l2_ptr:
                l2_ptr = l2_ptr.next

            if prev is not None:
                prev.next = start_node
            else:
                temp_start = start_node
            
            prev = start_node

        return temp_start


"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        l1_ptr = l1
        l2_ptr = l2

        temp_start = None
        start_node = None
        prev = None

        while l1_ptr is not None and l2_ptr is not None:
            temp_val = l1_ptr.val + l2_ptr.val

            temp_val += carry
            
            carry = temp_val // 10
            temp_val = temp_val % 10

            start_node = ListNode(temp_val)

            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next

            if prev is not None:
                prev.next = start_node
            else:
                temp_start = start_node
            
            prev = start_node


        while l1_ptr is not None:
            temp_val = carry + l1_ptr.val

            carry = temp_val // 10
            temp_val = temp_val % 10

            start_node = ListNode(temp_val)

            l1_ptr = l1_ptr.next

            if prev is not None:
                prev.next = start_node
            else:
                temp_start = start_node
            
            prev = start_node
        
        while l2_ptr is not None:
            temp_val = carry + l2_ptr.val

            carry = temp_val // 10
            temp_val = temp_val % 10

            start_node = ListNode(temp_val)

            l2_ptr = l2_ptr.next

            if prev is not None:
                prev.next = start_node
            else:
                temp_start = start_node
            
            prev = start_node
        
        if carry > 0:
            start_node = ListNode(carry)
            prev.next = start_node

        return temp_start
"""
