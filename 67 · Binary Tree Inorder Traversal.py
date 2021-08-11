"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root: return []

        result = []
        stack = []

        # 先處理左邊
        while root:
            stack.append(root)
            root = root.left
        
        while stack:
            curNode = stack.pop()
            result.append(curNode.val)

            # 處理右邊
            if curNode.right:
                curNode = curNode.right
                while curNode:
                    stack.append(curNode)
                    # append 左邊先於 root
                    curNode = curNode.left
        return result
