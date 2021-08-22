"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.maxSum = float('-inf')
    
    def maxPathSum(self, root):
        # write your code here
        if root is None:
            return 0
        self.helper(root)
        return self.maxSum
    
    def helper(self, node):
        if node is None:
            return 0
        
        # 分別處理左右子樹的最大值
        maxLeft = self.helper(node.left)
        maxRight = self.helper(node.right)

        self.maxSum = max(self.maxSum, maxLeft + maxRight + node.val)

        # 用來處理左右子樹的最大值，最後返回不會用到
        currentMax = max(maxLeft, maxRight) + node.val
        if currentMax < 0:
            return 0
        else:
            return currentMax
