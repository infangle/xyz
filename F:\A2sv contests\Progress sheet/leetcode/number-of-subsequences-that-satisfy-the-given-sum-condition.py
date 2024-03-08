class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mod = pow(10, 9) + 7
        nums. sort()
        l, r = 0, n -1 
        cnt = 0

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                x = r - l
                cnt += pow(2, x)
                l += 1

        return cnt % mod

                






        