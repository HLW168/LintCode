"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        return self.__helper(root, node)

    def __helper(self, root, node):
        if root is None: return node
        if node.val < root.val:
            root.left = self.__helper(root.left, node)
        if node.val > root.val:
            root.right = self.__helper(root.right, node)
        return root
