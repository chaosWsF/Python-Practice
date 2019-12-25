class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x < 10:
            return True
        else:
            s = str(x)
        
        if s[::-1] == s:
            return True
        else:
            return False