class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        if (n % 4 == 0 and (n % 100 != 0 or n % 400 == 0 ) ):
            return True
        return False
