class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l <= r:
            mid = (l+r)//2
            start = bisect_left(citations, mid)
            if n - start >= mid:
                l = mid + 1
            else:
                r = mid - 1
                
        return r

