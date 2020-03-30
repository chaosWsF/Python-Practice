"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

Example 2:

    Input: pattern = "abba", str = "dog cat cat fish"
    Output: false

Example 3:

    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

Example 4:

    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern, str):
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        
        char_map = {}
        for p, s in zip(pattern, str_list):
            if p in char_map:
                if char_map[p] != s:
                    return False
            else:
                char_map[p] = s
        
        return len(set(str_list)) == len(char_map)

    def wordPattern2(self, pattern, str):
        return len(set(pattern)) == len(set(str.split())) == len(set(zip(pattern, str.split()))) if len(pattern) == len(str.split()) else False
