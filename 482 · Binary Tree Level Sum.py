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
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):
        # write your code here
        if root is None: return 0
        elif level == 1:
            return root.val
        return self.levelSum(root.left, level-1) + self.levelSum(root.right, level-1)
