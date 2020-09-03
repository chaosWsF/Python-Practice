"""
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers 
i >= 0 and j >= 0. Return a list of all powerful integers that have value less than or equal to bound. You 
may return the answer in any order. In your answer, each value should occur at most once.

Example 1:

    Input: x = 2, y = 3, bound = 10
    Output: [2,3,4,5,7,9,10]
    Explanation: 
        2 = 2^0 + 3^0
        3 = 2^1 + 3^0
        4 = 2^0 + 3^1
        5 = 2^1 + 3^1
        7 = 2^2 + 3^1
        9 = 2^3 + 3^0
        10 = 2^0 + 3^2

Example 2:

    Input: x = 3, y = 5, bound = 15
    Output: [2,4,6,8,10,14]

Note:
    1. 1 <= x <= 100
    2. 1 <= y <= 100
    3. 0 <= bound <= 10^6
"""


class Solution:
    def powerfulIntegers(self, x, y, bound):
        def get_pow(a, bnd=bound):
            if a == 1:
                return [1]
            else:
                res, a_pow = [], 1
                while a_pow < bnd:
                    res.append(a_pow)
                    a_pow *= a
                
                return res
        
        x_lst = get_pow(x)
        y_lst = get_pow(y)
        return list(set(p + q for p in x_lst for q in y_lst if p + q <= bound))
