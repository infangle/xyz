class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        prefix_sum.append(nums[0])

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i-1] + nums[i])

        return prefix_sum