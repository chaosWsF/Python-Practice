"""
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input 
string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Note that an empty string is also considered valid.

Example 1:

    Input: "()"
    Output: true

Example 2:

    Input: "()[]{}"
    Output: true

Example 3:

    Input: "(]"
    Output: false

Example 4:

    Input: "([)]"
    Output: false

Example 5:

    Input: "{[]}"
    Output: true
"""


class Solution:
    def isValid(self, s):
        # TODO
    
    def isValid2(self, s):
        """use replace"""
        if not s:
            return True

        if len(s) % 2 == 1:
            return False

        pars = {'(': ')', '[': ']', '{': '}'}
        while s:
            flag = 0
            for par in pars.items():
                par = ''.join(par)
                if par in s:
                    s = s.replace(par, '')
                else:
                    flag += 1
            
            if flag == 3:
                return False
        else:
            return True
