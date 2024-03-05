# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal => strictly increasing

        def inorder(root):
            if not root:
                return []
            left = inorder(root.left)
            right = inorder(root.right)
            ans = []
            ans.extend(left) #extend the values from the left subtree
            ans.append(root.val) #appending the root of the subtree
            ans.extend(right) #extending the values from the right subtree
            return ans
        trav = inorder(root)
        for i in range(len(trav)-1):
            if trav[i] >= trav[i+1]:
                return False
        return True