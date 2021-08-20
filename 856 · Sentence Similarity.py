class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        # write your code here
        if (not (len(words1) == len(words2))):
            return False

        # 映射關係 --> 建立 dict
        mp = {}

        # 先遍歷 pairs 去看 word 之間的關係
        for i in range(len(pairs)):
            # 用 set 去儲存相對應的值，因為 set 是可以存非重複的無序數據
            S = set()
            # 去檢查 map 裡面有沒有這個值，有的話就加入集合裡面
            if (not (mp.get(pairs[i][0]) == None)):
                S = mp[pairs[i][0]]    
            S.add(pairs[i][1])
            mp[pairs[i][0]] = S

        for i in range(len(words1)):
            if (words1[i] == words2[i]):
                continue
            # words1 是索引， words2 是相對應的值 & words2 是索引， words1 是相對應的值
            if ((mp.get(words1[i]) == None) or words2[i] not in mp[words1[i]]) and ((mp.get(words2[i]) == None) or words1[i] not in mp[words2[i]]):
                return False
        return True
