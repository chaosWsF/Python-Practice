"""
Given n non-negative integers representing an elevation map where 
the width of each bar is 1, compute how much water it is able to 
trap after raining.


The above elevation map is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
section) are being trapped. Thanks Marcos for contributing this 
image!

Example:

    Input: [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
"""


class Solution:
    def trap(self, height):
        """Stack"""
        if not height:
            return 0
        
        area = 0
        stack = []
        for h in height:
            if not stack:
                stack.append(h)
            elif len(stack) == 1:
                if stack[0] <= h:
                    stack = [h]
                else:
                    stack.append(h)
            elif h < stack[0]:
                stack.append(h)
            else:
                area += len(stack) * stack[0] - sum(stack)
                stack = [h]
        
        return area
