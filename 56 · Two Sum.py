class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        res = []
        # 利用 dict 去存 key & value 
        d = dict()
        # 遍歷 numbers
        for i in range(len(numbers)):
            # 如果 target - number 沒有在 dict 裡面就存 number
            if target - numbers[i] not in d:
                d[numbers[i]] = i
            else:
                res.append(d[ target - numbers[i]])             
                res.append(i)
        return res
