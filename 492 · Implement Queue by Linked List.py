class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.before_head = LinkedListNode(-1)
        self.tail = self.before_head

    def enqueue(self, item):
        # write your code here
        self.tail.next = LinkedListNode(item)
        # 更新隊尾
        self.tail = self.tail.next

    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.before_head.next is None:
            return -1
        # 頭節點，要出去的節點
        head_val = self.before_head.next.val
        self.before_head = self.before_head.next

        return head_val
