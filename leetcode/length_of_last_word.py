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
    def lengthOfLastWord(self, s):
        """split string first"""
        str_list = s.split(' ')
        while str_list:
            if str_list[-1]:
                return len(str_list[-1])
            else:
                str_list.pop()
        else:
            return 0
