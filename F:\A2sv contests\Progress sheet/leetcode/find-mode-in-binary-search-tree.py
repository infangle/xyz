# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
            # in-order traversal :left, root, right
            if not root:
                return []
            left = inorderTraversal(root.left)
            right = inorderTraversal(root.right)
            ans = []
            ans.extend(left) #extend the values from the left subtree
            ans.append(root.val) #appending the root of the subtree
            ans.extend(right) #extending the values from the right subtree
            return ans
        
        nodes = inorderTraversal(root) 
        cnt = Counter(nodes)
        max_freq = max(cnt.values())
        res = []
        for key, val in cnt.items():
            if val == max_freq:
                res.append(key)
        return res

