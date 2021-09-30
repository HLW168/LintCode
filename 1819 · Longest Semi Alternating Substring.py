class Solution:
    """
    @param s: the string
    @return: length of longest semi alternating substring
    """
    def longestSemiAlternatingSubstring(self, s):
        # write your code here
        n = len(s)
        if n < 3:
            return n
        res, cnt = 0, 0
        left = 0
        # 固定左邊指針，然後移動右邊指針
        for right in range(n):
            if right > 0 and s[right] == s[right-1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt == 3:
                # 如果集滿三個那麼左邊就從右邊 - 1 開始
                left = right - 1
                cnt = 2
        
            res = max(res, right-left+1)

        return res
