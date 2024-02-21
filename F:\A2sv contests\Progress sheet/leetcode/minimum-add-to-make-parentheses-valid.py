class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openning = 0
        closing = 0
        for b in s:
            if b == '(':
                openning += 1
            else:
                if openning > 0:
                    openning -= 1
                else:
                    closing += 1

        return (openning + closing)
        