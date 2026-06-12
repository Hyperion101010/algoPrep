class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
            The crux of the problem is we traverse from left to right.
            For each point we maintain a farthest point we are able to travel till that index.
            Now if the farthest point we are able to travel is at the end of over then its possible to visit the array.
            Now if the farthest point leads us to 0 and the number is 0 and its less than the length of nums - 1 then False.
            In all other cases we are going to find a solution.
        """

        farthest_point = -1e9

        for i in range(len(nums)):
            farthest_point = max(farthest_point, i + nums[i])
            if farthest_point >= len(nums) - 1:
                return True
            
            # Need to evaluate the condition where the maximum reachable point 
            # till now is leading to 0.
            if farthest_point == i and nums[i] == 0 and i < len(nums) - 1:
                return False

        if farthest_point >= len(nums) - 1:
            return True
        
        return False
