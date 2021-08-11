class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        #先找到左括號
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            strs = []
            # 拿到左括號到右括號裡面的組
            while stack and stack[-1] != '[':
                strs.append(stack.pop()) 
            #跳過左括號拿到數字
            stack.pop()
            repeats = 0
            base = 1 #為了十位數做準備
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0'))*base
                base *= 10
            stack.append(''.join(reversed(strs))*repeats)
        return ''.join(stack)
