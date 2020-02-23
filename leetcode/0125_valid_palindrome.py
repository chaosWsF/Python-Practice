"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:

    Input: "race a car"
    Output: false
"""


class Solution:
    def isPalindrome1(self, s):
        """two pointers (44ms)"""
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True

    def isPalindrome2(self, s):
        """filter firstly (32ms)"""
        if not s:
            return True
        
        f = filter(str.isalnum, s)
        s = "".join(f).lower()
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - 1 - i]:
                return False
        
        return True

    def isPalindrome3(self, s):
        """builtin (28ms)"""
        s = "".join(filter(str.isalnum, s)).lower()
        return s == s[::-1]
