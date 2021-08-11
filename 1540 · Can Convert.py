class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        # Write your code here
        if (s == None and t == None): return True
        if (s == None or t == None or len(s) < len(t)): return False
        indexT = 0
        for indexS in range(len(s)):
            if s[indexS] == t[indexT]:
                indexT += 1
                if indexT == len(t):
                    return True
        return False
