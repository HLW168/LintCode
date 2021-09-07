"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        # 遞歸出口
        if root is None: return 0

        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        if root.left and root.right:
            return min(leftDepth, rightDepth) + 1
        else:
            return max(leftDepth, rightDepth) + 1
