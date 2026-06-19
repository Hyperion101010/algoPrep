class Solution:
    def minOperations(self, nums: list[int]) -> int:
        mx = -1
        sm = 0

        for each_idx in range(len(nums)):

            # If we found an element which is increasing then decide to make it greater.
            if each_idx > 0 and nums[each_idx - 1] < nums[each_idx]:
                if nums[each_idx - 1] < mx:

                    # Select the most best choice, either max - last to make it max
                    # or current - last
                    sm += min(mx - nums[each_idx - 1], nums[each_idx] - nums[each_idx - 1])

            # Let's update the max only if its not the last element.
            if nums[each_idx] > mx and each_idx != len(nums) - 1:
                mx = nums[each_idx]

        # The cases that we miss are;
        # If the last element was still less than the mx.
        if len(nums) > 1:
            if nums[each_idx] < mx:
                sm += mx - nums[each_idx]
        
        return sm
