class Solution:
    def rob(self, nums: List[int]) -> int:
        lkup = [-1 for i in range(len(nums))]
        self.ln = len(nums)
        self.nm = nums
        a1 = self.vst(0, 0, lkup[:])
        a2 = self.vst(1, 1, lkup[:])
        return max(a1, a2)

    def vst(self, start_idx, idx, lkup):
        if idx > self.ln - 1:
            return 0
        
        """
            The logic of house robber is as same as visiting either the current house
            then visiting house + 2 or house + 3 so that they are not adjacent houses.

            Only painful case is [1, 2, 3]
            In such scenario we can choose 1 but then we have to skip 3.
            What if we choose 3 then let's skip choosing 1.

            So this edge case needs to be handled.
            What we do is, maintain a start_index that tracks where you started from,
            then if we hit the end of the array,
            we compare it with start index value to see which array value maximizes our result.
            Thus, finally we return our answer.
        """
        if start_idx == 0 and idx == self.ln - 1 and self.ln > 1:
            if self.nm[start_idx] < self.nm[self.ln - 1]:
                return self.nm[self.ln - 1] - self.nm[start_idx]
            else:
                return 0
        
        if lkup[idx] > -1:
            return lkup[idx]
        
        lkup[idx] = self.nm[idx] + max(self.vst(start_idx, idx + 2, lkup), self.vst(start_idx, idx + 3, lkup))
        return lkup[idx]
