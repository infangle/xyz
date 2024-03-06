class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low, high = 1, x
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            sq = mid ** 2
            if sq == x:
                return mid
            elif sq > x:
                high = mid - 1
            else:
                ans = mid
                low = mid + 1
                
        return ans