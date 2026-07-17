class Solution:
    def traverse(self, r, c, t, visited):
        if r > self.r_len or c > self.c_len or r < 0 or c < 0:
            return False
        
        if visited[r][c] is not None:
            return visited[r][c]
            
        if self.grid[r][c] > t:
            visited[r][c] = False
            return False
        
        if r == self.r_len and c == self.c_len:
            visited[r][c] = True
            return True
        
        visited[r][c] = False
        res = False
        for each_move in self.moves:
            res = res or self.traverse(r + each_move[0], c + each_move[1], t, visited)

        visited[r][c] = res
        
        return res


    def swimInWater(self, grid: List[List[int]]) -> int:
        self.moves = [
            [0, -1],
            [0, 1],
            [1, 0],
            [-1, 0]
        ]

        mn = 1e9
        mx = 0
        for each_r in grid:
            for each_ele in each_r:
                mn = min(mn, each_ele)
                mx = max(mx, each_ele)
        
        lft = mn
        rgt = mx

        self.r_len = len(grid) - 1
        self.c_len = len(grid[0]) - 1

        md = 0

        self.grid = grid

        while rgt - lft >= 0:
            md = (lft + rgt) // 2

            visited = []
            for _ in range(len(grid)):
                visited.append([None for _ in range(len(grid[0]))])

            if not self.traverse(0, 0, md, visited):
                lft = md + 1
            else:
                rgt = md - 1
        
        return lft
