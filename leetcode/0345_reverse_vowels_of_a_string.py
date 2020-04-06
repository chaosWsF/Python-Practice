"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

    Input: "hello"
    Output: "holle"

Example 2:

    Input: "leetcode"
    Output: "leotcede"

Note:
    The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s):
        s = list(s)
        vowels = set('aeiouAEIOU')
        head = 0
        tail = len(s) - 1
        while head < tail:
            if (s[head] in vowels) and (s[tail] in vowels):
                s[head], s[tail] = s[tail], s[head]
                head += 1
                tail -= 1
            elif s[head] in vowels:
                tail -= 1
            elif s[tail] in vowels:
                head += 1
            else:
                head += 1
                tail -= 1
        
        return ''.join(s)
