"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param t: the root of tree
    @return: return a string
    """
    def tree2str(self, t):
        # write your code here
        s = str(t.val)
        haveLeft = False

        # 遍歷子樹
        if t.left is not None:
            haveLeft = True
            s += '(' + self.tree2str(t.left) + ')'
        if t.right is not None:
            if not haveLeft:
                s += '()'
            s += '(' + self.tree2str(t.right) + ')'
        
        return s
