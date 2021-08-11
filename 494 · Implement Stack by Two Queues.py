from collections import deque

class Stack:
   
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.queue1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        for _ in range(len(self.queue1)-1):
            val = self.queue1.popleft()
            self.queue2.append(val)
        val = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return val

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        val = self.pop()
        self.push(val)
        return val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not self.queue1
