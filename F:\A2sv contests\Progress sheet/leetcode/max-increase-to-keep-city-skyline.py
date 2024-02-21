class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r_max = [0] * n
        c_max = [0] * n
        for r in range(n):
            for c in range(n):
                r_max[r] = max(r_max[r], grid[r][c])
                c_max[c] = max(c_max[c], grid[r][c])
        
        inc = 0
        for r in range(n):
            for c in range(n):
                incr = min(r_max[r], c_max[c])
                inc += (incr - grid[r][c]) 
        return inc

