class Solution:
    """
    @param names: a string array
    @return: a string array
    """
    def nameDeduplication(self, names):
        # write your code here
        # 先遍歷，把名字加進去 dict
        # 再用 list append 的方式 append Key
        d = dict()
        res = []
        for i in range(len(names)):
            names[i] = names[i].lower()
            if names[i] not in d:
                d[names[i]] = 1
            else:
                d[names[i]] += 1
        for k in d.keys():
            res.append(k)
        res.sort()
        
        return res
