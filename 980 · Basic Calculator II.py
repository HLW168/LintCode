class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here

        stack = []
        num = 0
        sign = '+'

        for i, c in enumerate(s):
            #print('i', i)
            if c.isdigit():
                #print('before', num)
                num = 10*num + int(c)
                #print('num',num)
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = c
                # 如果不是连续 number 需考虑十进位
                num = 0
            #print('stack',stack)
        return sum(stack)
