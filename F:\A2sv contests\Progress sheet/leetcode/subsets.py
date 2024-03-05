class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx, sub):
            if idx > len(nums): #maximum subarry length = length(nums)
                return
            
            ans.append(sub[:])

            for i in range(idx, len(nums)):
                backtrack(i+1, sub + [nums[i]])

        backtrack(0, [])
        return ans


