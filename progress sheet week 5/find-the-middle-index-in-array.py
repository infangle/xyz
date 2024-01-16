class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum=0
        suffixSum=sum(nums)
        for i in range(len(nums)):
            suffixSum-=nums[i]
            if prefixSum == suffixSum:
                return i
            prefixSum += nums[i]
        return -1