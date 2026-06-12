class Solution:
    def jump(self, nums: List[int]) -> int:
        last_idx = 0
        steps = 0

        """
            The crux of solving this question is greedy approach.
            The greedy approach is choosing maximum (farthest) jump possible from the current end of the jump.
            So for each we cover the maximum possible.
            Then from that position we check for that idx + nums[i] where i in range(range of jump)
            idx + nums[i] for each index i shows in that range how much father we can jump.

            So for jump we select the next number which can lead to the maxmium jump.
            Thus, in this way we greedily select the best choice.
        """
        while last_idx < len(nums) - 1:
            idx = last_idx

            # If we already have a precomputation of the large value then lets use it.
            mx = -1

            # If choosing current index causes to finish the work then break.
            if idx + nums[idx] >= len(nums) - 1:
                steps += 1
                break

            # Traverse from last known index to next index and also store the result.
            for i in range(idx + 1, min(len(nums) - 1, idx + nums[idx] + 1)):
                if i + nums[i] >= mx:
                    mx = i + nums[i]
                    last_idx = i
            
            steps +=1

        return steps
