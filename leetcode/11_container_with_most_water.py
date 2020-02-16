class Solution:
    def maxArea(self, height):

        n = len(height)
        if n < 2:
            return 0
        
        i = 0
        j = n - 1
        area = min(height[i], height[j]) * (j - i)

        while i < j:
            area = max(area, min(height[i], height[j]) * (j - i))
            if (i + 1 < n) and (height[i] <= height[j]):
                i += 1
            else:
                j -= 1

        return area