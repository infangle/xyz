class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        valid = 0
        nums = sorted(nums)
        for i in range(len(nums)-1, 1, -1):
            target = nums[i]
            l, r = 0, i-1
            while l < r:
                if nums[l] + nums[r] > target:
                    valid += (r - l)
                    r -= 1
                else:
                    l += 1

        return valid
