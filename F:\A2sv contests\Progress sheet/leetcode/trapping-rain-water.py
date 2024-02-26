class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        lmax, rmax = [0] * n, [0] * n
        lmax[0], rmax[-1] = height[0], height[-1]

        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])

        trapped_water = 0
        for i in range(n):
            min_height = min(lmax[i], rmax[i])
            trapped_water += max(0, min_height - height[i])

        return trapped_water


  