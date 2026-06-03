class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        self.nums = nums
        return self.quickselect(l, r, k)

    def get_partition(self, l, r):
        # Using last index as the pivot point for our parition
        # Need to compare all elements with this pivot point and then replace.
        # If element less than pivot it stays on left half
        # If element greater than pivot then the pivot moves towards the element.
        # So we can do this by always swapping element when the element is greater than pivot.
        partition_num = self.nums[r]
        begin_idx = l

        for idx in range(l, r):
            if self.nums[idx] <= partition_num:
                self.nums[begin_idx], self.nums[idx] = self.nums[idx], self.nums[begin_idx]
                begin_idx+=1
        

        self.nums[begin_idx], self.nums[r] = self.nums[r], self.nums[begin_idx]

        return begin_idx


    def quickselect(self, l, r, k):
        idx = self.get_partition(l, r)

        if idx == len(self.nums) - k:
            return self.nums[idx]
        
        if idx > len(self.nums) - k:
            return self.quickselect(l, idx - 1, k)
        else:
            return self.quickselect(idx + 1, r, k)
        
        return -1
