class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = set()
        tot = 0
        top = float('-inf')

        def backtrack(idx, comb, tot, top):
            if tot == target:
                ans.add(tuple(sorted(comb[:])))
                return
            if tot > target:
                return

            for i in range(idx, len(candidates)):
                if candidates[i] == top:
                    continue
                comb.append(candidates[i])
                tot += candidates[i]
                backtrack(i+1, comb, tot, top)
                top = comb.pop()
                tot -= candidates[i]

        backtrack(0, [], tot, top)
        return list(ans)

