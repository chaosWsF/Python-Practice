"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that 
can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
    Assume the length of given string will not exceed 1,010.
Example:
    Input: "abccccdd"
    Output: 7
    Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s):
        res = 0
        for freq in Counter(s).values():
            if freq % 2 == 0:
                res += freq
            else:
                res += freq - 1
        
        return res if len(s) == res else res + 1
    
    def longestPalindrome2(self, s):
        return 2 * sum(x // 2 for x in Counter(s).values()) + any(x % 2 for x in Counter(s).values())
