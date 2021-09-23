"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if head is None:
            return True
        # 判斷長度是奇數還是偶數
        count = self.count(head)
        # 找中間的 node
        middle_node = self.middle(head)
        # reverse
        if count % 2 == 1:
            slow = self.reverse(middle_node)
        else:
            slow = self.reverse(middle_node.next)
        # 比較前後段
        while slow:
            if slow.val != head.val:
                return False
            else:
                slow = slow.next
                head = head.next             
        return True
                 
    def count(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
    def middle(self, head):
        slow = head
        fast = head       
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next         
        return slow
       
    def reverse(self, node):
        curt = None
        while node:
            temp = node.next
            node.next = curt       
            curt = node
            node = temp
        return curt
