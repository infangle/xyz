class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        per = []
        def backtrack():
            if len(per) == len(nums):
                ans.append(per[:])
            for num in nums:
                if num not in per:
                    per.append(num)
                    backtrack()
                    per.pop()

        backtrack()
        return ans

            