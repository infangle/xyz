# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # pre-order traversal :root, left, right
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        ans = []
        ans.append(root.val) #appending the root of the subtree
        ans.extend(left) #extend the values from the left subtree
        ans.extend(right) #extending the values from the right subtree
        return ans
        

         