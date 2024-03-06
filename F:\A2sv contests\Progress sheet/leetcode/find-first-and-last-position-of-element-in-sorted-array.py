class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return (bisect_left(nums, target), (bisect_right(nums, target) - 1))
        # left, right = 0, len(nums)-1

        # def firstpos(left, right):
        #     ans1 = -1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             ans1 = mid
        #             right = mid - 1
        #         elif nums[mid] < target:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
                    
        #     return ans1

        # def lastpos(left, right):
        #     ans2 = -1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if nums[mid] == target:
        #             ans2 = mid
        #             left = mid + 1
        #         elif nums[mid] > target:
        #             right = mid - 1
        #         else:
        #             left = mid + 1
        #     return ans2

        # return [firstpos(left, right), lastpos(left, right)]
            
