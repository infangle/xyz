class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r = k
        sub_sum = sum(nums[:k]) 
        max_avg = sub_sum/k
        while r < len(nums):
            
            sub_sum -= nums[r - k]
            sub_sum += nums[r]
            max_avg = max(max_avg, sub_sum/k)
            r += 1
        return max_avg

        