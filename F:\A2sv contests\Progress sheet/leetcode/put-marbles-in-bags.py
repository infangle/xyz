class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        marbles = []
        
        for i in range(1, len(weights)):
            marbles.append(weights[i] + weights[i-1])

        marbles = sorted(marbles)
        n = len(marbles)
        mini = sum(marbles[:k-1])
        maxi = sum(marbles[n-k+1:])
        return maxi - mini
