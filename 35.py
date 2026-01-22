class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lst = sorted(nums)
        lft = 0
        rgt = len(nums) - 1
        md = 0
        idx = len(nums)
        # We run a normal binary search but also tracking the index of the array.
        # First idx will start from right most position.
        # Then we only update idx when right pointer is reduced.
        while lft <= rgt:
            md = int((lft + rgt) / 2)
            if target == nums[md]:
                return md
            if target < nums[md]:
                rgt = md - 1
                idx = md
            else:
                lft = md + 1
        return idx
