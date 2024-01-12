class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_points = sum(cardPoints)
        mini = inf
        l = 0
        r = n-k
        window = sum(cardPoints[:n-k])
        mini = min(mini, window)

        while r < n:
            window += (cardPoints[r] - cardPoints[l])
            print(window)
            r += 1 
            l += 1
            
            mini = min(mini, window)

        return total_points - mini

            
