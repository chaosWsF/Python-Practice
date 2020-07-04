"""
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, 
find the smallest element in the list that is larger than the given target. Letters also wrap around. For example, 
if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:

    Input: letters = ["c", "f", "j"], target = "a"
    Output: "c"

    Input: letters = ["c", "f", "j"], target = "c"
    Output: "f"

    Input: letters = ["c", "f", "j"], target = "d"
    Output: "f"

    Input: letters = ["c", "f", "j"], target = "g"
    Output: "j"

    Input: letters = ["c", "f", "j"], target = "j"
    Output: "c"

    Input: letters = ["c", "f", "j"], target = "k"
    Output: "c"

Note:
    1. letters has a length in range [2, 10000].
    2. letters consists of lowercase letters, and contains at least 2 unique letters.
    3. target is a lowercase letter.
"""

import bisect


class Solution:
    def nextGreatestLetter1(self, letters, target):
        """Binary Search"""
        letters = list(dict.fromkeys(letters))
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        elif target == letters[0]:
            return letters[1]
        else:
            i, j = 0, len(letters) - 1
            while i <= j:
                k = (i + j) // 2
                if letters[k] > target:
                    j = k
                elif letters[k] == target:
                    return letters[k+1]
                else:
                    i = k + 1

            return letters[j]

    def nextGreatestLetter2(self, letters, target):
        """Linear Search"""
        for s in letters:
            if s > target:
                return s
        
        return letters[0]
    
    def nextGreatestLetter3(self, letters, target):
        """from target's loop"""
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        else:
            letters = set(letters)
            for i in range(ord(target)+1, 123):
                tmp = chr(i)
                if tmp in letters:
                    return tmp

    def nextGreatestLetter4(self, letters, target):
        """bisect module"""
        i = bisect.bisect_right(letters, target)
        return letters[i] if i < len(letters) else letters[0]
