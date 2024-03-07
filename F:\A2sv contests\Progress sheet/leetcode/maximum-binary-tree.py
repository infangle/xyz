# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        def findmax(nums, low, high):
            maxi = float('-inf')
            idx = -1
            while low <= high:
                if nums[low] > maxi:
                    maxi = nums[low]
                    idx = low
                low += 1
            return idx

        def rec(nums, low, high):
            if low > high:
                return
            x = findmax(nums, low, high)
            node = TreeNode(nums[x])
            node.left = rec(nums, low, x-1)
            node.right = rec(nums, x+1, high)
            return node

        if not nums:
            return None
        else:
            return rec(nums, 0, len(nums)-1)


            
