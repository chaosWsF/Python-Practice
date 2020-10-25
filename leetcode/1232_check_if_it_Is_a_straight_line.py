"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents 
the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:

https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg

    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:

https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg

    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    1. 2 <= coordinates.length <= 1000
    2. coordinates[i].length == 2
    3. -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    4. coordinates contains no duplicate point.
"""


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        n = len(coordinates)
        if n == 2:
            return True
        
        x_0, y_0 = coordinates[0]
        x_1, y_1 = coordinates[1]
        if x_0 == x_1:
            return all(coordinates[i][0] == x_0 for i in range(2, n))
        elif y_0 == y_1:
            return all(coordinates[i][1] == y_0 for i in range(2, n))
        
        def slope(p, x=x_0, y=y_0):
            if p[0] == x:
                return float('inf')
            else:
                return (p[1] - y) / (p[0] - x)
        
        k = (y_1 - y_0) / (x_1 - x_0)
        return all(slope(coordinates[i]) == k for i in range(2, n))
