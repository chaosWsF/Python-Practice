"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all 
in the range [-10000, 10000] (inclusive).

Example:
    Input: [[0,0],[1,0],[2,0]]
    Output: 2
    Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
from collections import Counter
import numpy as np
from scipy.spatial.distance import pdist, squareform


class Solution:
    def numberOfBoomerangs1(self, points):    # 612ms
        res = 0
        for p in points:
            d = {}
            for q in points:
                if q != p:
                    dx = p[0] - q[0]
                    dy = p[1] - q[1]
                    dsq = dx * dx + dy * dy
                    if dsq in d:
                        res += d[dsq]
                        d[dsq] += 1
                    else:
                        d[dsq] = 1
        
        return res * 2
    
    def numberOfBoomerangs2(self, points):    # 592ms
        return sum(m * (m - 1) for x1, y1 in points for m in Counter((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) for x2, y2 in points).values())

    def numberOfBoomerangs3(self, points):    # 312ms
        def dist_counter(dis):
            m = np.unique(dis, return_counts=True)[1]
            return np.sum(m * (m - 1))
        
        return sum(dist_counter(x) for x in squareform(pdist(np.array(points))))
