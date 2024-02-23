from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        l, r = 0, 0
        # building the first window
        while r< k:
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            r += 1
        # first window ans
        ans.append(queue[0])
        l += 1
        while r < len(nums):   
            # removing the outdated maximum
            if nums[l-1] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[r]:
                queue.pop()
            queue.append(nums[r])
            ans.append(queue[0])
            r += 1
            l += 1
            
        return ans
            

        