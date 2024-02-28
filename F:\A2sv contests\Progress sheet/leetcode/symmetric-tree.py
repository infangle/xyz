class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        return isMirror(root, root)
