"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Example 1:

    s = "leetcode"
    return 0.

Example 2:

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s):  # 52ms
        sc = Counter(s)
        for ss in sc:
            if sc[ss] == 1:
                return s.find(ss)
        
        return -1
