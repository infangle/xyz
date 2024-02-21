class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        l, r = 0, 1
        arrows = 0
        while r < len(points):
            if points[l][1] >= points[r][0]:
                r += 1
            else:
                arrows += 1
                l = r 
                r += 1
        return arrows + 1


