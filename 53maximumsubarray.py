class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        past_sum = 0
        mx = -1e9
        
        """
            The crux of this algorithm is Kadane's algorithm.
            We move from left to right and during this movement
            we maintain a maximum possible sum of all subarrays ending with the last index.
            1. So we maintain a past_sum that tells us the sum till the last index.
            And then we check if past sum was negative, no point in adding the current sum.
            Just start a new sum from the current element.
            2. If past sum is positive then there is benefit in adding the current element.
        """

        for i in range(len(nums)):
            if past_sum >= 0:
                past_sum += nums[i]
            else:
                past_sum = nums[i]
            
            mx = max(mx, past_sum)
        
        return mx
