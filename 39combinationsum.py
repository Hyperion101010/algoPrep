class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            We are going to solve this problem as much like the previous problem
            78 Subsets.

            Here, the logic is, we can take the array elements as many number of times.
            So what we can do is, write a simple loop to iterate and add all the elements from array.
            Then check if we meet the sum, then append it into the answer that we will display.
            Thus, then we finally create the answer and try all combinations.
            Then at last the output is stored and displayed.
        """
        self.op = []
        self.can = sorted(candidates)
        self.backtrack(0, [], target, 0)
        return self.op

    def backtrack(self, idx, arr, target, sm):
        # If checks to ensure that we stop when the array number that is to be taken
        # is not the one we want.
        if sm > target:
            return False
        if sm == target:
            # Here the answer is found
            # Thus now append the copy of arr and not arr into the output
            # append(arr) is a bug that I found
            # So appending arr[:] will work as expected.
            self.op.append(arr[:])
            return True
        # The for loop in this range will loop through the array and give the most desitred output.
        for i in range(idx, len(self.can)):
            arr.append(self.can[i])
            ans = self.backtrack(i, arr, target, sm + self.can[i])
            if ans == False:
                # Early exit
                arr.pop()
                break
            arr.pop()
