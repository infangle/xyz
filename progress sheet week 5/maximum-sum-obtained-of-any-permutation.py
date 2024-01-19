class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        kMod = 10**9 + 7
        freq = [0] * (len(nums) + 1)

        for l, r in requests:
            freq[l] += 1
            if r + 1 < len(freq):
                freq[r + 1] -= 1

        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)

        freq.sort(reverse=True)

        ans = 0

        for n, f in zip(nums, freq):
            ans += n * f

            ans %= kMod

        return ans
