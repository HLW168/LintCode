class Solution:
    """
    @param names: a string array
    @return: the string array
    """
    def DistinguishUsername(self, names):
        # Write your code here
        # 用字典紀錄次數
        # append 的時候可以 append 次數

        hashMap = {}
        result = []

        for name in names:
            if name in hashMap:
                count = hashMap[name] # 拿出次數
                hashMap[name] += 1
                result.append(name+str(count))
            else:
                hashMap[name] = 1
                result.append(name)

        return result
