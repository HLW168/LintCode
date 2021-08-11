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
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        newNode = ListNode(val)
        if head == None:
            return newNode
        elif head.val >= val:
            newNode.next = head
            return newNode
        else:
            node = head
            while node.next:
                if node.val < val and node.next.val >= val:
                    newNode.next = node.next
                    node.next = newNode
                    return head
                else:
                    node = node.next
            node.next = newNode #the biggest value
            return head
