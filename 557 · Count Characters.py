class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        # 創立一個 dict 結構
        d = dict()
        # 遍歷 str
        for i in range(len(str)):
            if str[i] not in d:
                d[str[i]] = 1
            else:
                d[str[i]] += 1
        return d
