class Solution:
    def findMin(self, nums: List[int]) -> int:
        lft = 0
        rgt = len(nums)-1

        # Now the problem description mentions that this problem has to be solved in log n
        # That means it will involve binary search implementation between two ends
        # We can consider that our minimum element will always lie in a range between l and r extreme ends
        # So we can do binary search with specific way to set the left and right pivot points.
        while lft <= rgt:
            md = int(lft + (rgt - lft)/2)

            # The condition to know that minimum element is found is when md + 1 > md and md - 1 < md
            # I am using modulus here since modulus can wrap around indices overflow for us.
            if nums[int((md + 1)% len(nums))] >= nums[md] and nums[int((md - 1)% len(nums))] >= nums[md]:
                return nums[md]
            # Now there is case when the pivot mid point is greater than the number at right
            # Then that means our element will lie in the right hand side of the midpoint.
            # Eg: 5 6 7 8 2 3 4 and lets say midpoint is 8
            # Now 8 is greater than 4 so it must lie in the right hand side of the point
            # Thus now we move left to md + 1
            elif nums[md] > nums[rgt]:
                lft = md + 1
            # In else scenario it lies on the left hand side of the midpoint.
            else:
                rgt = md - 1
        return -1
