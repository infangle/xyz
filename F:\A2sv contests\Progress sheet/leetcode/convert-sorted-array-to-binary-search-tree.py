# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1

        def create(nums, start, end):
            if start > end:
                return None
            mid = (start + end)//2

            node = TreeNode(nums[mid])
            node.left = create(nums, start, mid-1)
            node.right = create(nums,mid+1, end)
            return node

        return create(nums, start, end)
        