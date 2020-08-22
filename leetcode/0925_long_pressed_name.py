"""
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get 
long pressed, and the character will be typed 1 or more times. You examine the typed characters of the 
keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) 
being long pressed.

Example 1:

    Input: name = "alex", typed = "aaleex"
    Output: true
    Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:

    Input: name = "saeed", typed = "ssaaedd"
    Output: false
    Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.

Example 3:

    Input: name = "leelee", typed = "lleeelee"
    Output: true

Example 4:

    Input: name = "laiden", typed = "laiden"
    Output: true
    Explanation: It's not necessary to long press any character.

Constraints:
    1. 1 <= name.length <= 1000
    2. 1 <= typed.length <= 1000
    3. The characters of name and typed are lowercase letters.
"""

from itertools import groupby


class Solution:
    def isLongPressedName1(self, name, typed):
        i = j = 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        
        if i < len(name):
            return False
        else:
            while j < len(typed):
                if typed[j] == typed[j-1]:
                    j += 1
                else:
                    return False
        
            return True
    
    def isLongPressedName2(self, name, typed):
        lst_1 = [(s, len(list(g))) for s, g in groupby(name)]
        lst_2 = [(s, len(list(g))) for s, g in groupby(typed)]
        return all(s_1 == s_2 and x_1 <= x_2 for (s_1, x_1), (s_2, x_2) in zip(lst_1, lst_2)) if len(lst_1) == len(lst_2) else False
