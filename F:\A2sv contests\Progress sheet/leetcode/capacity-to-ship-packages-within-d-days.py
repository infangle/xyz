class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        def possible(mid):
            i = 0
            for ind in range(days):
                cur = 0
                while i < len(weights) and cur + weights[i] <= mid:
                    cur += weights[i]
                    i += 1
            if i >= len(weights):
                return True
                
            return False
        ans = 0
        while low <= high:
            mid = (low+high)// 2
            if possible(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans