class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        tot = 0
        def backtrack( idx, comb, tot):
            if tot == target:
               ans.add(tuple(sorted(comb[:])))
               return
            if tot > target:
                return
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                tot += candidates[i]
                backtrack(i, comb, tot)
                comb.pop()
                tot -= candidates[i]


            
        backtrack(0, [], tot)
        return list(ans)
