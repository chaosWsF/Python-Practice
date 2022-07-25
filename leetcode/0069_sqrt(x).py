"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to
be a non-negative integer.

Since the return type is an integer, the decimal digits are
truncated and only the integer part of the result is returned.

Example 1:

    Input: 4
    Output: 2

Example 2:

    Input: 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since 
                 the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        l, r = 0, x
        while l <= r:
            mid = (l+r) // 2
            val = mid * mid
            if val <= x < val + 2*mid + 1:
                return mid
            elif val > x:
                r = mid
            else:
                l = mid
    
    def mySqrt1(self, x):
        """Not use it!"""
        return int(x**.5)
    
    def mySqrt2(self, x):
        """Newton's (Newton–Raphson) method"""
        if x == 0:
            return 0
        
        x_0 = 1 + x / 2
        while (int(x_0) * int(x_0) > x) or ((int(x_0) + 1) * (int(x_0) + 1) <= x):
            x_0 = (x_0 + x / x_0) / 2

        return int(x_0)

    def mySqrt3(self, x):
        """The Bisection Method (false position)"""
        i = 0
        j = x
        while i < j:
            m = (i + j) // 2
            if m * m > x:
                j = m - 1
            elif m * m == x:
                return m
            else:
                i = m + 1
        
        if i * i > x:
            return i - 1
        else:
            return i

    def mySqrt4(self, x):
        """The Secant Method"""
        if x == 0:
            return 0
        
        p_0 = 0
        p_1 = x
        p = p_1 - (p_1 * p_1 - x) / (p_1 + p_0)
        while (int(p) * int(p) > x) or ((int(p) + 1) * (int(p) + 1) <= x):
            p_0 = p_1
            p_1 = p
            p = p_1 - (p_1 * p_1 - x) / (p_1 + p_0)

        return int(p)

    def mySqrt5(self, x):
        """Horner's Method for (all) real zeros of polynomials"""
        if x == 0:
            return 0

        P_coeff = [1, 0, -x]
        x_0 = 1 + x / 2
        while (int(x_0) * int(x_0) > x) or ((int(x_0) + 1) * (int(x_0) + 1) <= x):
            Q_coeff = [P_coeff[0]]
            for i in range(1, len(P_coeff)):
                Q_coeff.append(P_coeff[i] + x_0 * Q_coeff[i - 1])

            b_0 = Q_coeff[-1]
            Q_coeff = Q_coeff[:-1]
            Q_x = Q_coeff[0]
            for j in range(1, len(Q_coeff)):
                Q_x = Q_coeff[j] + Q_x * x

            x_0 -= b_0 / Q_x

        return int(x_0)

# NOTE:
# 
# (1) The method of False Position (also called Regula Falsi) 
# generates approximations in the same manner as the Secant method,
# but it includes a test to ensure that the root is always bracketed
# between successive iterations.
# 
# (2) To circumvent the problem of the derivative evaluation in 
# Newton’s method, we introduce The Secant Method.
# 
# (3) To use Newton’s method to locate approximate zeros of a 
# polynomial P(x), we need to evaluate P(x) and P'(x) at specified
# values. Since P(x) and P'(x) are both polynomials, computational 
# efficiency requires that the evaluation of these functions be 
# done in the nested manner. Horner’s method incorporates this 
# nesting technique, and,as a consequence, requires only n 
# multiplications and n additions to evaluate an arbitrary 
# nth-degree polynomial.
# 
# (4) If you want to get complex zeros of polynomials, you can try 
# Müller’s Method.
