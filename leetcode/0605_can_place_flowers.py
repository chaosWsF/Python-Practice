"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, 
flowers cannot be planted in adjacent plots - they would compete for water and both would die. Given 
a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers 
rule.

Example 1:

    Input: flowerbed = [1,0,0,0,1], n = 1
    Output: True

Example 2:

    Input: flowerbed = [1,0,0,0,1], n = 2
    Output: False

Note:
    1. The input array won't violate no-adjacent-flowers rule.
    2. The input array size is in the range of [1, 20000].
    3. n is a non-negative integer which won't exceed the input array size.
"""

from math import ceil


class Solution:
    def canPlaceFlowers(self, flowerbed, n):    # 160ms
        m = len(flowerbed)
        if sum(flowerbed) + n > ceil(m / 2):
            return False
        else:
            n_flower = 0
            for i in range(m):
                if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == m - 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n_flower += 1
                
                if n_flower >= n:
                    return True
            
            return False
