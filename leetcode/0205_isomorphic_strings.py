"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:

    Input: s = "egg", t = "add"
    Output: true

Example 2:

    Input: s = "foo", t = "bar"
    Output: false

Example 3:

    Input: s = "paper", t = "title"
    Output: true

Note:
    You may assume both s and t have the same length.
"""


class Solution:
    def isIsomorphic1(self, s, t):
        def _helper(s):
            s_char = {}
            s_enc = []
            for ss in s:
                if ss not in s_char:
                    s_char[ss] = len(s_enc)
                
                s_enc.append(s_char[ss])
            
            return s_enc
        
        return _helper(s) == _helper(t)

    def isIsomorphic2(self, s, t):
        s_char = {}
        t_char = {}
        n_enc = 0
        for i in range(len(s)):
            ss = s[i]
            tt = t[i]
            if ss not in s_char:
                s_char[ss] = n_enc
            
            if tt not in t_char:
                t_char[tt] = n_enc
            
            if s_char[ss] != t_char[tt]:
                return False
            else:
                n_enc += 1
        
        return True

    def isIsomorphic3(self, s, t):        
        char_map = {}
        for i in range(len(s)):
            if s[i] in char_map:
                if char_map[s[i]] != t[i]:
                    return False
                
            else:
                char_map[s[i]] = t[i]
        
        return len(set(t)) == len(char_map)

    def isIsomorphic4(self, s, t):
        return len(set(s)) == len(set(t)) == len(dict(zip(s, t)))
