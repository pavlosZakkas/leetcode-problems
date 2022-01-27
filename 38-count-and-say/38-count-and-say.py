class Solution(object):
    
    
    def say(self, num):
        num_chars = str(num)
        
        counter_of_consecutive_chars = 1
        result = ''
        
        for i, char in enumerate(num_chars[1:], start=1):
            
            previous_char = num_chars[i-1]
            
            if char == previous_char:
                counter_of_consecutive_chars += 1
            else:
                result += str(counter_of_consecutive_chars) + previous_char
                counter_of_consecutive_chars = 1
            
        result += str(counter_of_consecutive_chars) + num_chars[-1]
        return result
    
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        
        return self.say(self.countAndSay(n-1))
    