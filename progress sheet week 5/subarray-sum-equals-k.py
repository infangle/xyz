class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumFreq = {0:1}

        ans = 0

        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum - k in sumFreq:
                ans += sumFreq[runningSum - k]
                
            sumFreq[runningSum] = sumFreq.get(runningSum, 0) + 1

        return ans
            
