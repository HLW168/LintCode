"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode
    @return: return a boolean
    """
    def checkEqualTree(self, root):
        # write your code here
        # 預設一個 map 來記錄值
        self.mp = {}
        # 紀錄整棵樹的 sum
        sum = self.dfs(root)
        # edge case 討論 sum = 0 的情況
        if (sum == 0):
            return self.mp[0] > 1
        # sum 是偶數 且 sum/2 是的值是存在的
        return sum % 2 == 0 and not self.mp.get[sum/2] == None

    def dfs(self, root):
        if (root == None): return 0

        sum = root.val + self.dfs(root.left) + self.dfs(root.right)
        # 不存在這個值就存起來
        if (self.mp.get(sum) == None):
            self.mp[sum] = 1
        # 已經有這個值就加一
        else:
            self.mp[sum] += 1
        
        return sum
