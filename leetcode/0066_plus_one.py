"""
Given a non-empty array of digits representing a non-negative 
integer, plus one to the integer.

The digits are stored such that the most significant digit is 
at the head of the list, and each element in the array contain 
a single digit.

You may assume the integer does not contain any leading zero, 
except the number 0 itself.

Example 1:

    Input: [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123.

Example 2:

    Input: [4,3,2,1]
    Output: [4,3,2,2]
    Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        digits[-1] += 1
        while i >= 0:
            if digits[i] < 10:
                return digits
            
            digits[i] -= 10
            if i > 0:
                digits[i-1] += 1
            else:
                return [1] + digits
            
            i -= 1
        
        return digits
    
        # # lazy one
        # return [int(s) for s in str(int(''.join([str(i) for i in digits]))+1)]
    
    def plusOne1(self, digits):
        """directly plus one, then calibrate"""
        i = len(digits) - 1
        digits[i] += 1
        while i >= 0:
            if digits[i] < 10:
                return digits
            else:
                digits[i] -= 10
                if i > 0:
                    digits[i - 1] += 1
                else:
                    digits = [1] + digits
            
            i -= 1
        
        return digits

    def plusOne2(self, digits):
        """find 9"""
        n = len(digits)
        i = n - 1
        j = 0
        while i >= 0:
            while i - j >= 0:
                if digits[i - j] == 9:
                    j += 1
                else:
                    i -= j
                    digits[i] += 1
                    return digits[:i+1] + [0] * j
            i -= j

        return [1] + [0] * n
