class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [num for num in range(1,10)]
        ans = set()
        tot = 0
        top = float('-inf')

        def backtrack(idx, comb, tot, top):
            if len(comb) == k:
                if tot == n:
                    ans.add(tuple(sorted(comb[:])))
                    return

            if tot > n:
                return

            for i in range(idx, len(nums)):
                comb.append(nums[i])
                tot += nums[i]
                backtrack(i+1, comb, tot, top)
                top = comb.pop()
                tot -= nums[i]

        backtrack(0,[],tot, top)
        return list(ans)


