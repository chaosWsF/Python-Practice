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

        str_list = s.split()
        while str_list:
            if str_list[-1]:
                return len(str_list[-1])
            else:
                str_list.pop()
        else:
            return 0

    def lengthOfLastWord2(self, s):
        """two pointers (reverse)"""
        if not s:
            return 0

        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            else:
                sub_len = 1
                while i - sub_len >= 0:
                    if s[i - sub_len] == ' ':
                        break
                    else:
                        sub_len += 1
                return sub_len
        else:
            return 0

    def lengthOfLastWord3(self, s):
        """use str.rstrip"""
        s = s.rstrip()
        if s:
            return len(s[::-1].split(maxsplit=1)[0])
        else:
            return 0
