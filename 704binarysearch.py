class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = 0
        lft = 0
        rgt = len(nums)-1

        # We got to check till rgt and lft are equal so that mid is also checked properly.
        while rgt >= lft:
            mid = int(lft + (rgt - lft)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                rgt = mid - 1
            else:
                lft = mid + 1
        return -1
