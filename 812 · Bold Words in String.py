class Solution:
    """
    @param words: the words
    @param S: the string
    @return: the string with least number of tags
    """
    def boldWords(self, words, S):
        # Write your code here
        bold = set()
        for w in words:
            i, end = S.find(w,0), -1
            while i >= 0:
                bold.update(range(max(i, end + 1), i + len(w)))
                end, i = i + len(w)-1, S.find(w,i+1)
                    
        res = ''
        for i in range(len(S)):
            # 有在 set 裡面的都要加上 <b></b>
            if i in bold and i - 1 not in bold: res += '<b>'
            res += S[i]
            if i in bold and i + 1 not in bold: res += '</b>'
        return res
