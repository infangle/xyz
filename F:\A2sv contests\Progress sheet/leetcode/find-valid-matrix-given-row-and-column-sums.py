class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid=[]
        for i in range(len(rowSum)):
            grid.append([0]*len(colSum))
        minn=min(rowSum)
    

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                grid[r][c]=min(rowSum[r],colSum[c])
                rowSum[r]-=grid[r][c]
                colSum[c]-=grid[r][c]
                

        return grid