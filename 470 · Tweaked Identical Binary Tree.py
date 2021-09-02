"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):
        # write your code here
        return self.dfs(a,b)

    def dfs(self, a, b):
        if a is None and b is None: return True
        if (a and not b) or (not a and b): return False
        if a.val != b.val: return False

        ll_rr = self.dfs(a.left, b.left) and self.dfs(a.right, b.right)
        lr_rl = self.dfs(a.left, b.right) and self.dfs(a.right, b.left)

        return ll_rr or lr_rl
