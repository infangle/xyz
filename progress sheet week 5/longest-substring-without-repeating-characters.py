class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        sub = set()
        longest = 1
        # edge case
        if len(s) == 0:
            return 0
        # for
        for r in range(len(s)):
            # while
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            # update
            longest = max(longest, len(sub))
        return longest


        