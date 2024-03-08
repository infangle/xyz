class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        def possible(mid):
            k = 0
            for p in piles:
                k += ceil(p/mid)
                
            return k <= h
        ans = 0
        while low <= high:
            mid = (low+high)// 2
            if possible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans