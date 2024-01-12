class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l = 0
        r = 0
        score = 0
        subarray = set()
        maxi = 0

        # for
        for r in range(len(nums)):
            score += nums[r]

        # while
            while nums[r] in subarray:
                subarray.remove(nums[l])
                score -= nums[l]
                l += 1

            # update

            subarray.add(nums[r])
            maxi = max(maxi, score)
                
        return maxi
        