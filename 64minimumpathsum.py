class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        lkup = []
        self.g = grid
        for r in range(len(self.g)):
            lkup.append([10000001 for c in self.g[r]])
        
        self.r = len(grid)
        self.c = len(grid[0])
        a = self.vst(0, 0, lkup)
        return a
    
    def vst(self, r, c, lkup):
        """
            If we return 0 as in usual case we are actually affecting the minimum condition.
            So in our case what we will do is returning a big enough number for out of bound condition
            In such cases we will not consider this path as it should not have been added anyways.
        """
        if r > self.r - 1 or c > self.c - 1:
            return 100000
        
        # We hit the end of the path thus lets return the value.
        if self.r - 1 == r and self.c - 1 == c:
            lkup[self.r - 1][self.c - 1] = self.g[r][c]
            return lkup[self.r - 1][self.c - 1]
        
        # Default case for lookup to work, this means lookup is already ready.
        if lkup[r][c] < 10000001:
            return lkup[r][c]
        
        # Lookup stored and can be used ahead.
        lkup[r][c] = self.g[r][c] + min(self.vst(r + 1, c, lkup), self.vst(r, c + 1, lkup))

        return lkup[r][c]
