class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 1)

        for l, r, res in bookings:
            seats[l-1] += res
            seats[r] -= res
        
        for i in range(1, n):
            seats[i] = seats[i-1] + seats[i]

        return seats[:-1]

        