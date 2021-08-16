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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        isBST, minNode, maxNode = self.divideConquer(root)
        return isBST
    def divideConquer(self, root):
        if root is None:
            return True, None, None
        
        leftisBST, leftMin, leftMax = self.divideConquer(root.left)
        rightisBST, rightMin, rightMax = self.divideConquer(root.right)

        if not leftisBST or not rightisBST:
            return False, None, None
        if leftMax is not None and leftMax >= root.val:
            return False, None, None
        if rightMin is not None and rightMin <= root.val:
            return False, None, None

        minNode = leftMin if leftMin is not None else root.val
        maxNode = rightMax if rightMax is not None else root.val

        return True, minNode, maxNode 
