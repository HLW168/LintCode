"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if not head or not head.next: return head
        # 保存第2个节点
        temp = head.next
        # 第3个节点放递归
        head.next = self.swapPairs(head.next.next)
        # 第2节点连第1节点
        temp.next = head

        return temp
