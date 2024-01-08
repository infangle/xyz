class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        l = 0
        r = 0
        v = 0
        maxi = 0

        while r < len(s):
            if s[r] in vowels:
                v += 1

            if r - l + 1 > k:  # Shrink the window from the left
                if s[l] in vowels:
                    v -= 1
                l += 1

            r += 1
            maxi = max(maxi, v)
        
        return maxi