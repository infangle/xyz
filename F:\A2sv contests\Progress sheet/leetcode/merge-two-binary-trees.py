# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return
        elif not root1:
            return root2
        elif not root2:
            return root1
        else:
            tree = TreeNode(root1.val + root2.val)
            tree.left = self.mergeTrees(root1.left, root2.left)
            tree.right = self.mergeTrees(root1.right, root2.right)
        return tree

        
        