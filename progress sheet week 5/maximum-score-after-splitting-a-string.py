class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 0
        nums = []
        for n in s:
            nums.append(int(n))

        tot = sum(nums)
        ans = -inf
        pre = 0
        # exclude the last element of nums from the loop
        for num in nums[:-1]:
            pre += num
            if num == 0:
                zeros += 1
            ans = max(ans,tot - pre + zeros )
            
        return ans
