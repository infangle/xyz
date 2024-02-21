class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        ans = 0
        for ch, c in freq.items():
            if c % 2 == 0:
                ans += c
            else:
                ans += (c-1)
        
        if ans < len(s):
            ans += 1
        return ans
        