class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        existing_positive_nums = set(
            filter(lambda x: x>0 ,nums)
        )
        
        for num in range(1, len(existing_positive_nums) + 1):
            if num not in existing_positive_nums:
                return num
        
        return len(existing_positive_nums) + 1