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
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        lists = []
        if not root: return lists
        self.dfs(root, lists)
        return lists
    
    def dfs(self, node, lists):
        # 讓下標跟 level 一樣
        # 遞歸出口
        if node is None: return -1
        # 遞歸拆解，後序遍歷
        left_level = self.dfs(node.left, lists)
        right_level = self.dfs(node.right, lists)
        curr_level = max(left_level, right_level) + 1
        self.add_to_lists(lists, curr_level, node.val)
        return curr_level

    def add_to_lists(self, lists, curr_level, value):
        if curr_level == len(lists):
            lists.append([])
        lists[curr_level].append(value)
        return lists
