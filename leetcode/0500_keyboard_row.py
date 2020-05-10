r"""
Given a List of words, return the words that can be typed using letters of alphabet on only 
one row's of American keyboard like the image below.

https://assets.leetcode.com/uploads/2018/10/12/keyboard.png
 
Example:

    Input: ["Hello", "Alaska", "Dad", "Peace"]
    Output: ["Alaska", "Dad"]

Note:
    You may use one character in the keyboard more than once.
    You may assume the input string will only contain letters of alphabet.
"""


class Solution:
    def findWords1(self, words):
        d = {
            'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1, 
            'a': 2, 's': 2, 'd':2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2, 
            'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3
        }

        res = []
        for s in words:
            letters = set(s.lower())
            row = d[letters.pop()]
            flag = True
            for letter in letters:
                if d[letter] != row:
                    flag = False
                    break
            
            if flag:
                res.append(s)
        
        return res

    def findWords2(self, words):
        row1 = set('qwertyuiop')
        row2 = set('asdfghjkl')
        row3 = set('zxcvbnm')
        res = []
        for s in words:
            tmp = set(s.lower())
            if not ((tmp - row1) and (tmp - row2) and (tmp - row3)):
                res.append(s)
        
        return res
