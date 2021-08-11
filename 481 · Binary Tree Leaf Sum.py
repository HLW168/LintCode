"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: An integer
    """
    def leafSum(self, root):
        # write your code here
        if root is None: return 0
        if not root.left and not root.right:
            return root.val
        return self.leafSum(root.left) + self.leafSum(root.right)
