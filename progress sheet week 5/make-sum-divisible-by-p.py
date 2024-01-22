class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ans = len(nums)
        
        total = sum(nums) % p
        
        if total == 0:
            return 0
        
        prefix = [0]
        for num in nums:
            prefix.append((prefix[-1] + num) % p)
        
        freq = {}
        
        for i, rem in enumerate(prefix):
            if (rem - total) % p in freq:
                ans = min(ans, i - freq[(rem - total) % p])
            
            freq[rem] = i
        
        return -1 if ans == len(nums) else ans
