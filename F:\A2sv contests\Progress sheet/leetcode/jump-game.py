class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_idx = len(nums) - 1
        steps = 0
        
        for i in range(len(nums)):
            if i > steps:
                return False
            steps = max(steps, i + nums[i])
            
        return True



        