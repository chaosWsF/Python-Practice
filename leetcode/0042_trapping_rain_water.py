"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it is able to 
trap after raining.

Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""


class Solution:
    def trap(self, height):
        """Two pointers, stack (44ms)"""
        if not height:
            return 0
        
        area = 0
        i = 0
        j = 1
        trapped = []
        while j < len(height):
            if height[i] <= height[j]:
                area += len(trapped) * height[i] - sum(trapped)
                i = j
                trapped = []
            else:
                trapped.append(height[j])
            j += 1
        else:
            if trapped:
                area += self.trap([max(trapped)] + trapped)
        
        return area
