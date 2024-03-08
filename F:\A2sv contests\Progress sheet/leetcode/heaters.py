class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        mini = 0
        maxi = max(houses[-1], heaters[-1])

        def heat(mid):
            ht, hs = 0, 0 
            while ht < len(heaters) and hs < len(houses):
                l, r = heaters[ht] - mid, mid + heaters[ht] 
                if houses[hs] >= l and houses[hs] <= r:
                    hs += 1
                else:
                    ht += 1
                
            return hs >= len(houses)
        ans = 0         
        while mini <= maxi:
            mid = (mini + maxi) // 2
            if heat(mid):
                ans = mid
                maxi = mid - 1 
            else:
                mini = mid + 1
        return ans

            