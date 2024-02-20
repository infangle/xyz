class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patch = 0
        target = 1
        l = 0
        while target <= n:
            if l < len(nums) and nums[l] <= target: 
                target += nums[l]
                l += 1
            else:
                target *= 2
                patch += 1
            
                
        return patch