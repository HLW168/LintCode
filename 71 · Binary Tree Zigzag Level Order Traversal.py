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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        lists = []
        if not root: return lists
        
        # 一層層遍歷，用兩個 stack 交替存放
        stack = []
        next_stack = []

        stack.append(root)
        # 代表當前層存放順序
        left_to_right = True
        # bfs
        while len(stack) != 0:
            #紀錄當前層的 nodes
            nodes = []
            # 為了取出當前層的所有 nodes 並擴展下一層放進 next_stack
            while len(stack) !=0:
                # 彈出一個 node
                curr_node = stack.pop()
                if curr_node is None: 
                    continue
                # 不是 None 則可能拓展 left 和 right 兩個子樹
                nodes.append(curr_node.val)

                # 判斷當前層的遍歷方向
                if left_to_right:
                    next_stack.append(curr_node.left)
                    next_stack.append(curr_node.right)
                else:
                    next_stack.append(curr_node.right)
                    next_stack.append(curr_node.left)

            # 翻轉方向
            left_to_right = not left_to_right
            
            # nodes 並不是空 list
            if len(nodes) > 0:
                lists.append(nodes)
            
            # stack 的迭代
            stack = next_stack
            next_stack = []
        return lists


