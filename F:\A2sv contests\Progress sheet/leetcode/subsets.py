class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(idx, sub):
            # base case
            if len(nums) < idx:
                return
            ans.append(sub[:])
            
            for i in range(idx, len(nums)):
                sub.append(nums[i])
                backtrack(i+1, sub)
                sub.pop()

            
        backtrack(0, [])
        return ans


