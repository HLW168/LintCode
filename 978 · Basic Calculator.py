class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        stack = []
        result = 0
        number = 0
        sign = 1

        for c in s:
            if c in '1234567890':
                number = 10*number + int(c)
            elif c == '+':
                result += sign * number
                number = 0
                sign = 1
            elif c == '-':
                result += sign * number
                number = 0
                sign = -1
            elif c == '(':
                # 先把 result 和 sign 存起來
                stack.append(result)
                stack.append(sign)
                # 初始化
                sign = 1
                result = 0
            elif c == ')':
                result += sign * number
                number = 0
                result *= stack[-1] #括號前的符號，+ or -
                result += stack[-2] #括號前的 result
                stack = stack[:-2] #處理完這組括號號剩下的 stack
        
        #處理 for loop 結束後還沒有被 result 加入或減去的 number
        result += sign * number
        return result
