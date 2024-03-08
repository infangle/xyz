class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        def possible(mid):
            i = 0
            for ind in range(k):
                cur = 0
                while i < len(nums) and cur + nums[i] <= mid:
                    cur += nums[i]
                    i += 1
            if i >= len(nums):
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