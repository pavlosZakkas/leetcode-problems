class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_chars = str(x)
        x_chars_reversed = x_chars[::-1]
        
        return x_chars == x_chars_reversed