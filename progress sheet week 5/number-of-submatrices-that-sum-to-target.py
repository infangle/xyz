class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j-1]
        ans = 0
        for i in range(n):
            for j in range(i, n):
                subarraySums = {0: 1}
                currSum = 0
                for k in range(m):
                    currSum += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    if currSum - target in subarraySums:
                        ans += subarraySums[currSum - target]
                    subarraySums[currSum] = subarraySums.get(currSum, 0) + 1
        return ans
