class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def backtrack( comb):
            if sum(comb) == target:
               ans.add(tuple(sorted(comb[:])))
               return
            if sum(comb) > target:
                return
            for candidate in candidates:
                comb.append(candidate)
                backtrack(comb)
                comb.pop()

            
        backtrack([])
        return list(ans)
