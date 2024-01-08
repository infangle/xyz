class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Left pointer
        r = len(nums) - 1  # Right pointer

        while k <= r:
            if nums[k] == val:
                nums[k] = nums[r]
                r -= 1
            else:
                k += 1

        return k