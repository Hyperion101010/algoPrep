class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # The logic to solve this problem is:
        # We can start counting from the least elements.
        # So for each lowest element we check the max consequent length possible.
        # For checking if the next elements are there we can use a set.
        # Eg. [100, 4, 200, 1, 3, 2]
        # So we check for only 1 and 100 since 1-1 = 0 and 100-1 does not exist.
        # Thus we have a O(n) method.
        lkup = set(nums)
        lst = []
        for i in lkup:
            if (i-1) in lkup:
                continue
            else:
                lst.append(i)

        if len(lst) == 0:
            return 0
        
        mx = 1
        for i in lst:
            idx = 0
            while i+idx in lkup:
                idx+=1
            mx = max(mx, idx)
        
        return mx
