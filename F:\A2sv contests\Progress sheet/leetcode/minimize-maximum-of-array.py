class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        prefixsum = [0]*len(nums)
        prefixsum[0] = nums[0]

        for i in range(1, len(nums)):
            prefixsum[i] = prefixsum[i-1] + nums[i]

        for i in range(len(prefixsum)):
            tot = math.ceil(prefixsum[i]/(i+1))
            ans = max(ans, tot)

        return ans
