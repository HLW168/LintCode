class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        # Write your code here
        # 當且僅當出現次數為奇數的字符個數為 0 或 1 時可以構成回文串
        # 紀錄出現的奇數次
        odd_cnt = 0
        # 紀錄字符的出現次數
        char_cnt = {}

        result = []

        for c in s:
            if c not in char_cnt:
                char_cnt[c] = 1
                odd_cnt += 1
            elif char_cnt[c] % 2 == 0:
                char_cnt[c] += 1
                odd_cnt += 1
            else:
                char_cnt[c] += 1
                odd_cnt -= 1
            if odd_cnt > 1:
                result.append(0)
            else:
                result.append(1)
        return result
