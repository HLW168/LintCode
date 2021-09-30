class Solution:
    """
    @param s: the string s
    @return: the number of operations at least
    """
    def numberOfOperations(self, s):
        # Write your code here
        charset = 'abcdefghijklmnopqrstuvwxyz'
        n = len(s)
        i, j = 0, n-1
        cnt = 0
        while i < j:
            cnt += abs(charset.find(s[i])-charset.find(s[j]))
            i += 1
            j -= 1
        return cnt
