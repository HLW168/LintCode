class Solution:
    """
    @param answers: some subset of rabbits (possibly all of them) tell 
    @return: the minimum number of rabbits that could be in the forest.
    """
    def numRabbits(self, answers):
        # write your code here
        d = dict()

        for i in range (len(answers)):
            if answers[i] in d:
                d[answers[i]] += 1
            else:
                d[answers[i]] = 1
        
        rabbit_num = 0
        # key 是兔子回答的數字， value 是這個數字出現的次數
        for k,v in d.items():
            num_per_group = k + 1
            reply_cnt = v
            # 有幾組
            num_of_group = reply_cnt // num_per_group  
            if reply_cnt %  num_per_group != 0:
                num_of_group += 1
            rabbit_num += num_of_group * num_per_group
        return rabbit_num  
