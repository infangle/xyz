class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        k = n // 4
        count = Counter(s)
        ans = n
        left = 0
        for right in range(n):
            count[s[right]] -= 1
            while left < n and count.get('Q', 0) <= k and count.get('W', 0) <= k and count.get('E', 0) <= k and count.get('R', 0) <= k:
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1
        return ans
