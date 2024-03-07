class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char_set =set(s)

        for i in range(len(s)):
            if s[i].lower()not in char_set or s[i].upper() not in char_set:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])

                return max(s1,s2, key = len)

        return s