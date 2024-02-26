class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        stack = []
        res = 0
        for i, a in enumerate(arr):
            while stack and a < stack[-1][1]:
                j, b = stack.pop()
                if stack:
                    left = j - stack[-1][0]
                else:
                    left = j + 1
                right = i - j 
                res = (res + b * left * right) % mod
            stack.append((i, a))

        while stack:
            j, n = stack.pop()
            if stack:
                left = j - stack[-1][0]
            else:
                left = j + 1
            right = len(arr) - j
            res = (res + n * left * right) % mod

        return res

