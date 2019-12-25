class Solution:
    def reverse(self, x: int) -> int:
        if -10 < x < 10:
            return x
        elif x <= -10:
            sig = -1
            x = -x
        else:
            sig = 1
        
        digits = []
        while x > 0:
            digits.append(x % 10)
            x = x // 10
        
        for i, d in enumerate(digits):
            x += d * 10 ** (len(digits)-1-i)
        
        if -2**31 <= x < 2**31:
            return sig * x
        else:
            return 0
