"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the tree
    @param val: the val which should be find
    @return: the node
    """
    def searchBST(self, root, val):
        # Write your code here.
        if root == None or root.val == val:
            return root
        if val < root.val:
            # 左子樹
            return self.searchBST(root.left, val)
        else:
            # 右子樹
            return self.searchBST(root.right, val)
