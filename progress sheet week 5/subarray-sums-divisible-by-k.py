class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0

        sumFreq = {0:1}

        runningSum = 0

        for i in range(len(nums)):
            runningSum += nums[i]
            if runningSum % k  in sumFreq:
                ans += sumFreq[runningSum % k]
                
            sumFreq[runningSum % k] = sumFreq.get(runningSum % k, 0) + 1

        return ans

        