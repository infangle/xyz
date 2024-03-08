class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxi = max(nums)
        mini = 1
        n =  len(nums)
        def ispossible(mid):
            i = 0
            cur = 0
            for num in nums: 
                cur += ceil(num / mid)
                    
            return cur <= threshold
        ans = 0
        while mini <= maxi:
            mid = (maxi+mini) // 2
            if ispossible(mid):
                ans = mid
                maxi = mid - 1
            else:                
               mini = mid + 1
        return ans
                