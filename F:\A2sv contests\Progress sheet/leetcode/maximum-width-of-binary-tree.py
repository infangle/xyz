# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 0
        queue = [(root, 0)]

        while queue:
            level = len(queue)
            left = queue[0][1]
            right = queue[-1][1]
            ans = max(ans, right - left + 1)
            for i in range(level):
                node, idx = queue.pop(0)
                if node.left:
                    queue.append((node.left, idx*2))
                if node.right:
                    queue.append((node.right, idx*2+1))

            for i in range(len(queue)):
                queue[i] = (queue[i][0], queue[i][1] - left)
        return ans
            