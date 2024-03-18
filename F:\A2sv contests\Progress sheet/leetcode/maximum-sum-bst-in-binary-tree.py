class NodeValue:
    def __init__(self, minNode, maxNode, Sum):
        self.maxNode = maxNode
        self.minNode = minNode
        self.Sum = Sum

class Solution:
    def largestBstHelper(self, node):
        if not node:
            return NodeValue(float('inf'), float('-inf'), 0)

        left = self.largestBstHelper(node.left)
        right = self.largestBstHelper(node.right)

        if left.maxNode < node.val and node.val < right.minNode:
            currSum=left.Sum+ right.Sum + node.val
            self.maxSum=max(self.maxSum,currSum)
            return NodeValue(min(node.val, left.minNode), max(node.val, right.maxNode),currSum)

        return NodeValue(float('-inf'), float('inf'), max(left.Sum, right.Sum))
    
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum=0
        ans=self.largestBstHelper(root).Sum 
        return self.maxSum