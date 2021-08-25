"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        # edge case
        if not head: return head

        dummy = ListNode(-1, head)
        cur = head
        while cur.next:
            if cur.val <= cur.next.val:
                cur = cur.next
            else:
                start = dummy
                while start.next.val <= cur.next.val:
                    start = start.next
                # 用 tmp 取出要排的值
                tmp = cur.next
                # cur 跳過要排的點
                cur.next = cur.next.next
                # 把 start.next 一串給要排的值連上
                tmp.next = start.next
                # 把 tmp 插在 start 後面
                start.next = tmp
        return dummy.next
