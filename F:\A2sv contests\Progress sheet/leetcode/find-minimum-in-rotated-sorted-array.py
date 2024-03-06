class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n - 1
        ans = float('inf')
        
        while low < high:
            mid = (low + high) // 2 
            if nums[mid] > nums[high]:
                ans = min(ans, nums[high])
                low = mid + 1
            else:
                ans = min(ans, nums[low])
                ans = min(ans, nums[mid])
                high = mid - 1
        
        if low == high:
            ans = min(ans, nums[low])
            ans = min(ans, nums[(low + 1)%n])
            ans = min(ans, nums[(low - 1)%n]) 


        return ans
        
