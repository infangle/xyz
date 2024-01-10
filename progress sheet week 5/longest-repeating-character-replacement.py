class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        l = 0
        maxi_len = 0

        # for
        for r in range(len(s)):
            chars[s[r]] += 1
            # while
            while (r-l+1)-max(chars.values()) > k :
                chars[s[l]] -= 1
                l += 1

            # update
            maxi_len = max(maxi_len, (r-l+1))

        return maxi_len


        