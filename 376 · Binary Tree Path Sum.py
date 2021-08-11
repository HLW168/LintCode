"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        if not root: return []
        res = []
        self.dfs(root, target, [], res)
        return res
    

    def dfs(self, root, target, path, res):
        # 空節點
        if root is None: return
        # 紀錄路徑
        path.append(root.val)
        # 最後一層的節點
        if not root.left and not root.right:
            if target == root.val:
                res.append(path[:])
            del path[-1]
            return
        self.dfs(root.left, target-root.val, path, res)
        self.dfs(root.right, target-root.val, path, res)
        # 不是最後一層的 path 也要往上走
        del path[-1]
