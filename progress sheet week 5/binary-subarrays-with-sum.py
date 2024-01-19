class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        subsum = {0: 1} 
        out = 0
        pref = 0

        for i in range(len(nums)):
            pref += nums[i]

            if pref - goal in subsum:
                out += subsum[pref - goal]
            subsum[pref] = subsum.get(pref, 0) + 1

        return out

