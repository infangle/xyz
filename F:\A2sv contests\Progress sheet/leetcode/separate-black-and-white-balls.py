class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        swaps = 0

        while l < r:
            if s[l] == '1' and s[r] == '1':
                r -= 1

            elif s[l] == '1' and s[r] == '0':
                swaps += r-l
                l += 1
                r -= 1
            else:
                l += 1
        return swaps