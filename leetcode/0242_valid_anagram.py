"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:

    Input: s = "rat", t = "car"
    Output: false

Note:
    You may assume the string contains only lowercase alphabets.
Follow up:
    What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

from collections import Counter


class Solution:
    def isAnagram1(self, s, t):        
        return sorted(s) == sorted(t)

    def isAnagram2(self, s, t):
        if len(s) != len(t):
            return False
        
        d_s = {}
        d_t = {}
        for ss, tt in zip(s, t):
            if ss in d_s:
                d_s[ss] += 1
            else:
                d_s[ss] = 1
            
            if tt in d_t:
                d_t[tt] += 1
            else:
                d_t[tt] = 1
        
        return d_s == d_t
    
    def isAnagram3(self, s, t):  # 28ms, 13MB
        return Counter(s) == Counter(t) if len(s) == len(t) else False
