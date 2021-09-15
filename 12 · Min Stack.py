class MinStack:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        # 存 number 和 min_val
        # 判斷 min_val
        min_val = min(number, self.stack[-1][1] if self.stack else number)
        self.stack.append((number, min_val))

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        val, _ = self.stack.pop() # 會彈出 number 和 最小值
        return val

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        # 把 min_val 放在最後一組 list 裡面
        _, min_val = self.stack[-1]
        return min_val
