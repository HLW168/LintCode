"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        # 沒有 head 或是 head 只有一個
        if not head or not head.next: return head
        # 找到中點做分類
        mid = self.find_mid(head)
        # 分三個鏈表，分別放 1.大於 mid / 2. 等於 mid / 3.小於 mid
        dummy_l, dummy_m, dummy_r = ListNode(-1), ListNode(-1), ListNode(-1)
        tail_l, tail_m, tail_r = dummy_l, dummy_m, dummy_r
        #遍歷鏈表做 partition
        while head:
            if (head.val < mid.val):
                tail_l.next = head
                tail_l = tail_l.next
            elif (head.val > mid.val):
                tail_r.next = head
                tail_r = tail_r.next
            else:
                tail_m.next = head
                tail_m = tail_m.next
            head = head.next
        # 遍歷結束後連上 None
        tail_l.next = None
        tail_m.next = None
        tail_r.next = None

        sorted_left = self.sortList(dummy_l.next)
        sorted_right = self.sortList(dummy_r.next)
        return self.conncet(sorted_left, dummy_m.next, sorted_right)

    def find_mid(self, head):
        # 利用雙指針來找中點，fast 走兩步
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def conncet(self, left, mid, right):
        # 把鏈表連起來
        # 先創建一個 dummy
        dummy = ListNode(-1, left)
        cur = dummy
        while cur.next:
            cur = cur.next
        # 遍歷完左邊的鍊表
        cur.next = mid
        while cur.next:
            cur = cur.next
        # 遍歷完中間的鏈表
        cur.next = right
        return dummy.next
