class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == 0:
            return self.countConsecutiveOnes(nums)
        
        l = 0  # Left pointer
        r = 0  # Right pointer
        output = 0

        while r < len(nums):
            if nums[r] == 0:
                k -= 1

            while k < 0:  # Shrink the window from the left
                if nums[l] == 0:
                    k += 1
                l += 1

            r += 1
            output = max(output, r - l)

        return output

    def countConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0

        return max_count