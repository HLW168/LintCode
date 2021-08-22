"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        # 空樹是任何樹的子樹
        if T2 is None:
            return True
        #空樹一定不是空樹的子樹
        if T1 is None:
            return False
        #如果兩樹的 value 相等，就互為子樹
        if self.isEqual(T1, T2):
            return True
        
        return self.isSubtree(T1.right, T2) or self.isSubtree(T1.left, T2)
    
    def isEqual(self, T1, T2):
        # 都是空樹
        if T1 is None and T2 is None:
            return True
        # 一個為空，一個不為空
        if T1 is None or T2 is None:
            return False
        # value 不相同
        if T1.val != T2.val:
            return False
        
        #兩者的左右子樹是否相同
        return self.isEqual(T1.left, T2.left) and self.isEqual(T1.right, T2.right)
