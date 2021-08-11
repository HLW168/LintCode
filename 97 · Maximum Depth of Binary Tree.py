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
    def maxDepth(self, root):
        # write your code here
        self.depth = 0
        self.traverse(root, 1)
        return self.depth

    def traverse(self, root, curDepth):
        if not root: return
        self.depth = max(self.depth, curDepth)
        self.traverse(root.left, curDepth + 1)
        self.traverse(root.right, curDepth + 1)
