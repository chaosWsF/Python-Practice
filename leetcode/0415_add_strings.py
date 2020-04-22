"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
    The length of both num1 and num2 is < 5100.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def addStrings(self, num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        
        i = 1
        carry = 0
        res = []
        while (i <= len(num2)) or (carry == 1):
            if i <= len(num2):
                tmp = int(num1[-i]) + int(num2[-i]) + carry
                if tmp > 9:
                    carry = 1
                    res.append(str(tmp - 10))
                else:
                    carry = 0
                    res.append(str(tmp))
            elif i <= len(num1):
                tmp = int(num1[-i]) + carry
                if tmp > 9:
                    carry = 1
                    res.append(str(tmp - 10))
                else:
                    carry = 0
                    res.append(str(tmp))
            else:
                carry = 0 
                res.append(str('1'))
            
            i += 1

        if len(res) < len(num1):
            return num1[:len(num1)-len(res)] + ''.join(res[::-1])
        else:
            return ''.join(res[::-1])
