class Solution(object):
    
    digits = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}

    def get_int_from(self, num_str):
        num = 0
        for digit, power in zip(num_str[::-1],  range(len(num_str))):
            num += self.digits[digit]  * (10**power)
            
        return num
        
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        

        num1_int = self.get_int_from(num1)
        num2_int = self.get_int_from(num2)
        return str(num1_int * num2_int)