class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def bestScoreAdvantage(lo, hi):
            if lo > hi:
                return 0
            return max(nums[lo] - bestScoreAdvantage(lo + 1, hi),
                       nums[hi] - bestScoreAdvantage(lo, hi - 1))

        return bestScoreAdvantage(0, len(nums) - 1) >= 0

