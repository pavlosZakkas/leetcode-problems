class Solution(object):

    def area_from(self, height, left, right):
        return min(height[left], height[right]) * (right - left)
    
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_index = 0
        right_index = len(height) - 1
        max_area = 0
        
        while left_index < right_index:
            current_area = self.area_from(height, left_index, right_index)
            max_area = max(max_area, current_area)
            
            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1
                
        return max_area
            