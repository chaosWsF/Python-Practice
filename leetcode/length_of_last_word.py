"""
Given a string s consists of upper/lower-case alphabets and empty 
space characters ' ', return the length of last word (last word 
means the last appearing word if we loop from left to right) in 
the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of 
non-space characters only.

Example:

    Input: "Hello World"
    Output: 5
"""


class Solution:
    def lengthOfLastWord1(self, s):
        """split string first"""
        if not s:
            return 0

        str_list = s.split(' ')
        while str_list:
            if str_list[-1]:
                return len(str_list[-1])
            else:
                str_list.pop()
        else:
            return 0

    def lengthOfLastWord2(self, s):
        """two pointers"""
        if not s:
            return 0

        sub_lens = []
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                sub_len = 1
                while i + sub_len < len(s):
                    if s[i + sub_len] == ' ':
                        break
                    else:
                        sub_len += 1
                i += sub_len
                sub_lens.append(sub_len)
        
        if not sub_lens:
            return 0
        else:
            return sub_lens[-1]
