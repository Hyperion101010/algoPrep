class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Two pointer method
        # Let's start with the left(first) pointer and keep a right(second) pointer
        # Now first move the first pointer towards the first occurence of val
        # Move the second pointer to the first occurence that we want to replace.
        # Now let's replace second with first pointer elements.
        # Now return the number of different elements count. 
        fp = 0
        sp = 0
        tmp = 0
        while fp < len(nums) and nums[fp] != val:
            fp +=1
        tmp = fp
        sp = fp
        while sp < len(nums) and nums[sp] == val:
            sp +=1
        while sp < len(nums):
            nums[fp] = nums[sp]
            fp +=1
            sp +=1
            tmp +=1
            if sp < len(nums):
                while sp < len(nums) and nums[sp] == val:
                    sp+=1
        return tmp
