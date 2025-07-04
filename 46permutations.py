class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.op = []
        self.nm = nums
        self.ln = len(nums)
        self.backtrack(0, 0, [], [False for i in range(self.ln)])
        return self.op
        
    def backtrack(self, idx, cnt, lkup, bool_lkup):
        """
            Base condition for the backtracking.
            Here we keep track of the array elements that we have visited.
            Only call recursively those array elements where we have not visited them in our lookup.
        """
        if cnt == self.ln:
            self.op.append(lkup[:])
            return

        """
            total_ct is the total number of times we need to run this combination,
            to check for all the possibilities.
        """
        total_ct = 0
        while total_ct < self.ln:
            """
                boolean lookup is an array used to visit the array places that we don't have considered in our logic.
                We do combinations of the array elements
                First we push the index that we consider into the array
                This index is then used to call its inside combinations.
                After we check all the possibilities of one index we consider the next element and go on moving forward.
                Thus we mark the boolean flag as visited or not as we push and pop from the list.
            """
            if bool_lkup[idx] is False:
                lkup.append(self.nm[idx])
                bool_lkup[idx] = True
                id2x = idx
                idx = (idx + 1) % self.ln
                self.backtrack(idx, cnt + 1, lkup, bool_lkup[:])
                bool_lkup[id2x] = False
                lkup.pop()
            else:
                idx = (idx + 1) % self.ln
            total_ct += 1

        return
