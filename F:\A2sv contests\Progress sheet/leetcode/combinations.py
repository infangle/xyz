class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [num for num in range(1, n+1)]
        ans = []

        def backtrack(i:int, comb:int):
            if len(comb) == k:
               ans.append(comb[:])
               return
            if i >= n:
                return

            backtrack(i+1, comb)
            comb.append(nums[i])
            backtrack(i+1, comb)
            comb.pop()


        backtrack(0, [])
        return ans

           