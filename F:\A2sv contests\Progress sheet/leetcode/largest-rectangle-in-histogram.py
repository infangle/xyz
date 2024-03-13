class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # increasing monotonic
        stack = []
        max_a = 0

        for idx, height in enumerate(heights):
            start = idx

            while stack and stack[-1][1] > height:
                i, h = stack.pop()

                max_a = max(max_a, (idx-i)*h)
                start = i
            stack.append((start, height))

        for index, height in stack:
            max_a = max(max_a, (len(heights)-index)*height)
            
        return max_a
