# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root,maxi,mini):
            if not root: 
                return maxi - mini
                
            maxi = max(root.val,maxi)
            mini = min(root.val,mini)
            left = traverse(root.left,maxi,mini)
            right = traverse(root.right,maxi,mini)
            return max(left,right)
        return traverse(root,-inf,inf)