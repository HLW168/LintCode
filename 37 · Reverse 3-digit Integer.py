class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # turn the number into String, after reverse, turn back to int 
        return int(str(number)[::-1])
