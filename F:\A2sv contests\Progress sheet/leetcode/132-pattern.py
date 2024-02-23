class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        valid = float('-inf')  

        for n in reversed(nums):
            if n < valid:
                return True  
            while stack and stack[-1] < n:
                valid = stack.pop()  
            stack.append(n)

        return False

# Example usage:
# nums = [3, 1, 4, 2]
# solution = Solution()
# print(solution.find132pattern(nums))  # Output: True
