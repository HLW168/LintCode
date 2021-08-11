class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        # str = s.split();
        # for i in range(len(str)): 
        #     if i == 0 and str[i] != ' ':
        #         str[i] = str[i].upper();
            
        #     if i != 0 and str[i] != ' ' and str[i - 1] == ' ':
        #         str[i] = str[i].capitalize();
      
        
        return s.title()
