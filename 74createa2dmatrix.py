class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lft = 0
        rgt = len(matrix)-1
        idx = -1
        while rgt >= lft:
            md = int(lft + (rgt - lft)/2)

            # In our case we are keeping track of the target to be within range of the whichever list we choose.
            # So we run a normal binary search, only this time the stopping criteria is now rango of values if the
            # midpoint satisfies this criteria
            # So then we will get the valid index which one to choose.
            if target >= matrix[md][0] and target <= matrix[md][len(matrix[0])-1]:
                idx = md
                break
            elif matrix[md][0] > target:
                rgt = md - 1
            else:
                lft = md + 1
    

        lft = 0
        rgt = len(matrix[idx]) - 1
        md = 0

        # Now run a normal binary search over the range you have and finish it.
        while rgt >= lft:
            md = int(lft + (rgt - lft)/2)
            if matrix[idx][md] == target:
                return True
            elif matrix[idx][md] > target:
                rgt = md - 1
            else:
                lft = md + 1
        return False
