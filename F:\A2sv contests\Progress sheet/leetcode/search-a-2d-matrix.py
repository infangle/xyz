class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l+r) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m -1
            else:
                break

        if not(l <= r):
            return False

        row = (l+r) // 2
        low, high = 0, len(matrix[0]) - 1

        while low <= high:
            mid = (low + high) // 2
            if target > matrix[row][mid]:
                low = mid + 1
            elif target < matrix[row][mid]:
                high = mid - 1
            else:
                return True

        return False