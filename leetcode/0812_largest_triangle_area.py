"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:

    Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    Output: 2
    Explanation: The five points are show in the figure below. The red triangle is the largest.

    https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png

Notes:
    1. 3 <= points.length <= 50.
    2. No points will be duplicated.
    3. -50 <= points[i][j] <= 50.
    4. Answers within 10^(-6) of the true value will be accepted as correct.
"""

import itertools
import numpy as np


class Solution:
    def largestTriangleArea1(self, points):
        def area(A, B, C):
            x_1, y_1 = A
            x_2, y_2 = B
            x_3, y_3 = C
            return 0.5 * abs(x_2 * y_3 - x_3 * y_2 - x_1 * y_3 + x_3 * y_1 + x_1 * y_2 - x_2 * y_1)
        
        return max(area(*selected) for selected in itertools.combinations(points, 3))

    def largestTriangleArea2(self, points):
        return max(
            abs(np.linalg.det(np.hstack((np.array(selected), np.ones((3, 1)))))) * 0.5 for selected in itertools.combinations(points, 3)
        )
