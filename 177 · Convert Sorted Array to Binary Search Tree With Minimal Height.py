"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
        if not A: return None

        middle = len(A) // 2
        root = TreeNode(A[middle])
        root.right = self.sortedArrayToBST(A[middle+1:])
        root.left = self.sortedArrayToBST(A[:middle])

        return root
