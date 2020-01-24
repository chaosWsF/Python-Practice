"""
Write a function to find the longest common prefix string amongst 
an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"

Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
  All given inputs are in lowercase letters a-z.
"""

class Solution:
    def longestCommonPrefix(self, strs):
        if (not strs) or ("" in strs):
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        n = 0
        str_n = set(s[n] for s in strs)
        while len(str_n) == 1:
            n += 1
            try:
                str_n = set(s[n] for s in strs)
            except IndexError:
                break
        
        return strs[0][:n]
