class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        max_len, table = 0, {n: True for n in num}
        
        for lo in num:
            if lo - 1 not in table:
                hi = lo + 1
                while hi in table: # hi in table is the start num of consecutive
                    hi += 1
                max_len = max(max_len, hi-lo)
        return max_len
