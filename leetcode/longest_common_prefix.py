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
        """use set to get common part"""
        if (not strs) or ("" in strs):
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        n = 0
        substr = set(s[n] for s in strs)
        while len(substr) == 1:
            n += 1
            try:
                substr = set(s[n] for s in strs)
            except IndexError:
                break
        
        return strs[0][:n]

    def longestCommonPrefix2(self, strs):
        """use nested loops"""
        if (not strs) or ("" in strs):
            return ""
        
        substr_0 = strs[0]

        if len(strs) == 1:
            return substr_0
        
        l = 0
        flag = True
        while l < len(substr_0):
            letter = substr_0[l]
            for substr in strs[1:]:
                if l >= len(substr):
                    flag = False
                    break

                if substr[l] != letter:
                    flag = False
                    break
            
            if flag == True:
                l += 1
            else:
                break

        return substr_0[:l]
