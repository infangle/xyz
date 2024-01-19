class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        destination = 0

        for p, f, t in trips:
            destination = max(destination, t)

        dist = [0] * (destination + 1)

        for p, f, t in trips:
            dist[f] += p
            dist[t] -= p
        
        for i in range(1, len(dist)):
            dist[i] = dist[i-1] + dist[i]

        for i in range(len(dist)):
            if dist[i] > capacity:
                return False
            
        return True
