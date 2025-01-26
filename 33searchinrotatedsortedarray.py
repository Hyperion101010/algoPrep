class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lft = 0
        rgt = len(nums) - 1
        idx = -1

        # In this particular problem we know that the elements are in a sorted order
        # Now when the elements are in the sorted order we first check which part is in sorted order (left or right part)
        while rgt >= lft:
            md = int(lft + (rgt - lft)/2)

            if nums[md] == target:
                idx = md
                break
            # Here checking if mid point of nums is greater than left, that means we have a sorted order array
            # Eg: 4 5 6 7 8 0 1 2
            # Half is 7
            # We check 8 is not present in left half so we just check right hand one
            elif nums[lft] <= nums[md]:
                # Now we check if target really falls in this condition
                # If it falls we need to check in the left hand side of the half
                if nums[lft] <= target and target <= nums[md]:
                    rgt = md - 1
                # If not then the target is present in the right hand side of the half
                else:
                    lft = md + 1
            # Now we check the condition where the reamining half is not a fully sorted array
            # Eg: 5 1 3
            # Half is 1
            else:
                # Here if target is 3 then we know it could be present in right hand side of things as its greater than mid and less than rgt
                if nums[md] <= target and target <= nums[rgt]:
                    lft = md + 1
                # Here in else case we know that it could be present in left hand side of things since its in lft
                else:
                    rgt = md - 1
        return idx
