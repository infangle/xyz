class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtrack(idx, sub):
            if idx >= len(nums):
                ans.add(tuple(sorted(sub[:])))
                return
            
            sub.append(nums[idx])
            backtrack(idx + 1, sub)
            sub.pop()
            backtrack(idx + 1, sub)
            return

        backtrack(0, [])
        ans = list(ans)
        ans.sort()
        return ans
