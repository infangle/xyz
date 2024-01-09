class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_count = 0
        f_count = 0
        l = 0
        r = 0
        max_length = 0

        while r < len(answerKey):
            if answerKey[r] == 'T':
                t_count += 1
            else:
                f_count += 1

            while min(t_count, f_count) > k:  
                if answerKey[l] == 'T':
                    t_count -= 1
                else:
                    f_count -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length