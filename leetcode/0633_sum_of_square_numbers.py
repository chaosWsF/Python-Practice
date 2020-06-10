"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b 
such that a ^ 2 + b ^ 2 = c.

Example 1:

    Input: 5
    Output: True
    Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

    Input: 3
    Output: False

"""


class Solution:
    def judgeSquareSum1(self, c):
        """idea from add two number, O(2*sqrt(c)), 284ms"""
        if c % 4 == 3:
            return False
        
        all_squared = set()
        i = 0
        while i * i <= c:
            all_squared.add(i * i)
            i += 1
        
        for x in all_squared:
            if (c - x) in all_squared:
                return True
        
        return False
    
    def judgeSquareSum2(self, c):    # 156ms
        """use sqrt, O(sqrt(c)), 156ms"""
        if c % 4 == 3:
            return False
        
        i = 0
        while i * i <= c:
            tmp = (c - i * i) ** 0.5
            if int(tmp) == tmp:
                return True
            else:
                i += 1
        
        return False

    def judgeSquareSum3(self, c):
        """number theory, 32ms"""    
        i = 2
        while i * i < c:
            r = 0
            if c % i == 0:
                while c % i == 0:
                    r += 1
                    c //= i
                
                if i % 4 == 3 and r % 2 == 1:
                    return False
            
            i += 1
        
        return c % 4 != 3
    
    def judgeSquareSum4(self, c):
        """binary search, O(sqrt(c) * log(c)), 1708ms"""
        if c % 4 == 3:
            return False
        elif c == 0:
            return True
        else:
            i = 0
            while i * i <= c:
                if self.isPerfectSquare(c - i * i):
                    return True
                else:
                    i += 1
                
            return False

    def isPerfectSquare(self, num):  # 16ms
        if (num % 4) not in [0, 1]:
            return False
        
        a = 1
        b = num
        while a <= b:
            c = (a + b) // 2
            tmp = c * c
            if tmp > num:
                b = c - 1
            elif tmp == num:
                return True
            else:
                a = c + 1
        
        return False
