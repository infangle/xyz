from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct_elements = set(nums)
        count = {}
        left = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

            while len(count) == len(distinct_elements):
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
                ans += len(nums) - i

        return ans