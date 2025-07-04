class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.op = [[]]
        self.nm = sorted(nums)
        self.ln = len(nums)
        self.backtrack(0, [])
        return self.op

    def backtrack(self, idx, arr):
        """
            Terminate the search if the index of the array is greater than the number.
        """
        if idx > self.ln - 1:
            return
        
        """
            The logic of this solution is,
            we first sort the elements to keep all duplicates together.
            Then for each element we call it recursively thus we will get all unique subsets under it.
            Then we call the elements that are duplicates only once,
            In this way we branch out properly. 
        """
        arr.append(self.nm[idx])
        self.op.append(arr[:])
        self.backtrack(idx + 1, arr)
        arr.pop()

        """
            Move our index pointer to the place where we skip the all repeating numbers of the current index.
            Cause these numbers followed by the index will already be considered.
            Thus we call backtrack on the next start of the number where it starts to repeat.  
        """
        while idx + 1 < self.ln and self.nm[idx + 1] == self.nm[idx]:
            idx += 1
        
        self.backtrack(idx + 1, arr)

        return
