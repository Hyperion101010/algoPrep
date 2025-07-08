class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m = m
        self.n = n
        lkup = []
        """
            Creating a 2D table for our lookup
        """
        for i in range(m):
            tmp = [-1 for j in range(n)]
            lkup.append(tmp)
        
        return self.vst(0, 0, lkup)

    def vst(self, r, c, lkup):
        if r > self.m - 1 or c > self.n - 1:
            return 0
        
        if r == self.m-1 and c == self.n-1:
            return 1
        
        if lkup[r][c] > -1:
            return lkup[r][c]
        
        """
            Each call either left or right is a path.
            So when we reach the end of the lookup table we know its a path, so return 1.
            Now finally we call for 2 different paths and measure if its possible to have the paths.
        """
        lkup[r][c] = self.vst(r + 1, c, lkup) + self.vst(r, c + 1, lkup)
        return lkup[r][c]
